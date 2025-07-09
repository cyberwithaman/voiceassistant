from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from .models import Conversation, Message, UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .engine import get_assistant_response
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone_number', 'bio']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

@login_required
def home(request):
    return render(request, 'assistant/home.html')

@login_required
def chat(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        conv_id = request.POST.get('conversation_id')
        if conv_id:
            conversation = get_object_or_404(Conversation, id=conv_id, user=request.user)
        else:
            conversation = Conversation.objects.create(user=request.user)
        Message.objects.create(conversation=conversation, sender='user', text=text)
        # Use LangChain/LangGraph engine for assistant response with context
        response_text = get_assistant_response(text, user=request.user, conversation=conversation)
        Message.objects.create(conversation=conversation, sender='assistant', text=response_text)
        return JsonResponse({'response': response_text, 'conversation_id': conversation.id})
    else:
        conversation = None
        if 'conversation_id' in request.GET:
            conversation = get_object_or_404(Conversation, id=request.GET['conversation_id'], user=request.user)
        return render(request, 'assistant/chat.html', {'conversation': conversation})

@login_required
def conversations_list(request):
    conversations = Conversation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'assistant/conversations_list.html', {'conversations': conversations})

@login_required
def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
    return render(request, 'assistant/conversation_detail.html', {'conversation': conversation})

@login_required
def delete_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
    if request.method == 'POST':
        conversation.delete()
        messages.success(request, 'Conversation deleted successfully.')
        return redirect('conversations_list')
    return render(request, 'assistant/delete_conversation.html', {'conversation': conversation})

@login_required
def settings_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('settings')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile
    }
    return render(request, 'assistant/settings.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def logout_view(request):
    """Custom logout view that handles both GET and POST requests"""
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        # For GET requests, show a logout confirmation page
        return render(request, 'registration/logged_out.html')
