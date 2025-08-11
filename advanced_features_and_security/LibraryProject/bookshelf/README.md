## Permissions and Groups Setup

Custom permissions added to Book model:
- can_view
- can_create
- can_edit
- can_delete

Groups:
- Viewers: [can_view]
- Editors: [can_view, can_create, can_edit]
- Admins: [all permissions]

Permission enforcement is done using `@permission_required` in views.
