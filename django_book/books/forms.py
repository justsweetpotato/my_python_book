#!/usr/bin/env python

from django import forms


class BookForm(forms.Form):
    text = forms.CharField(label="内容", required=True, max_length=4000)


class CryptoForm(forms.Form):
    text = forms.CharField(required=False, max_length=4000)
    key = forms.CharField(required=True, max_length=100)
    crypto_text = forms.CharField(required=False, max_length=4000)
