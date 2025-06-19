from django.http import HttpResponse
from django.contrib import admin
from django.shortcuts import redirect
from unfold.admin import ModelAdmin

class BaseAdmin(ModelAdmin):
    actions = ['export_as_csv']
    resource_class = None  # Each child admin should define this

    @admin.action(description="📤 Export selected records (CSV)")
    def export_as_csv(self, request, queryset):
        if not queryset.exists():
            self.message_user(request, "No records to export.", level='error')
            return redirect(request.META.get('HTTP_REFERER', '/admin/'))

        if not self.resource_class:
            self.message_user(request, "No resource_class defined for this admin.", level='error')
            return redirect(request.META.get('HTTP_REFERER', '/admin/'))

        try:
            resource = self.resource_class()
            export_data = resource.export(queryset)

            model_name = queryset.model.__name__.lower()
            response = HttpResponse(export_data.csv, content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={model_name}_export.csv'
            self.message_user(request, f"Exported {queryset.count()} records.", level='success')
            return response
        except Exception as e:
            self.message_user(request, f"Export failed: {str(e)}", level='error')
            return redirect(request.META.get('HTTP_REFERER', '/admin/'))
