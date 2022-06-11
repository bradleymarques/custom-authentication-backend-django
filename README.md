# How to create a custom authentication backend in Django

## Introduction

Django comes with
[built-in authentication backends](https://docs.djangoproject.com/en/4.0/topics/auth/)
that make it really easy to get started and meet most projects' needs. There are
also a slew of Django apps (such as [django-allauth](https://django-allauth.readthedocs.io/))
that have been written to integrate your Django application with identity
providers such as Google and GitHub. But when even these don't meet your
project's requirements, there is the option of creating your own custom
authentication backend. This sounds like a complicated thing to do, but is
actually really simple.

This tutorial will take you from absolute zero to a fully working authentication
system in Django. We'll also make it reusable so you can take it and plug it
into any other projects that you may have.

Note that will not be covered in this tutorial (but I will cover later) are:

+ Custom authorization schemes in Django
+ Building a custom REST API authentication backend in Django

## Starting the application

Let's start by creating our Django project:

```sh

```
