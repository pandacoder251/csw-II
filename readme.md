# Django Blog Project

A comprehensive Django blog application demonstrating core features, model management, views, templates, pagination, and email sharing.

## 1. Building a Blog Application

### Environment Setup
- Installing Python
- Creating a Python virtual environment
- Installing Django via pip

### Django Basics
- Overview of Django and its main components
- Understanding the Django architecture
- New features in Django 5
- Creating your first Django project
- Applying initial database migrations
- Running the development server
- Project settings overview
- Projects vs Applications

### Models
- Creating the blog data models
- Defining the `Post` model
  - Adding datetime fields
  - Default sort order
  - Adding a database index
  - Adding status field
  - Many-to-one relationships
- Creating and applying migrations

### Admin Site
- Creating a superuser
- Adding models to the admin site
- Customizing model display
- Adding facet counts to filters

### QuerySets and Managers
- Creating, updating, and deleting objects
- Retrieving and filtering objects
- Using field lookups, chaining filters, excluding objects
- Ordering, limiting, counting, and checking objects
- Complex lookups with Q objects
- Understanding QuerySet evaluation
- Creating custom model managers

### Views and Templates
- Building list and detail views
- Using `get_object_or_404` shortcut
- Adding URL patterns for views
- Creating templates for views
  - Base template
  - Post list template
  - Post detail template
- Understanding the request/response cycle
- Management commands used

---

## 2. Enhancing Your Blog and Adding Social Features

### Functional Enhancements
- Using canonical URLs for models
- Creating SEO-friendly URLs
- Modifying URL patterns and views

### Pagination
- Adding pagination to the post list view
- Creating pagination templates
- Handling pagination errors

### Class-Based Views
- Benefits of class-based views
- Using class-based views to list posts

### Email Sharing
- Creating forms with Django
- Handling forms in views
- Sending emails using Gmail SMTP
- Working with environment variables
- Rendering forms in templates


### Creating a model for comments
- Adding comments to the administration site
- Creating forms from models
---------------