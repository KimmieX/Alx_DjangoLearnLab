## API Testing Strategy

- Location: `api/test_views.py`
- Framework: Django REST Framework + unittest
- Coverage:
  - CRUD operations for Book model
  - Filtering, searching, ordering
  - Authentication and permission enforcement

### Running Tests
```bash
python manage.py test api