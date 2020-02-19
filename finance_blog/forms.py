"""
Django forms are incredibly useful for handling HTML forms gracefully, and all while
minimizing the bulky overhead of HTML + CSS + JS traditionally required in an HTML form.

TODO: Finish implementing
"""
from datetime import datetime
from django import forms


class CommentForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    # `sender` should meet interview project requirements
    sender = forms.CharField(null=True, blank=True, default="Anonymous")
    submitted = forms.DateTimeField(default=datetime.now, blank=True)
