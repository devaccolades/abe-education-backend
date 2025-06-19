from import_export import resources, fields, widgets
from .models import *

# BASE_URL = "http://127.0.0.1:8000" 
BASE_URL="https://admin.abeedu.com/"

class JobApplicationFormResource(resources.ModelResource):
    cv_file = fields.Field(
        column_name='cv_file',
        attribute='cv_file'
    )

    def dehydrate_cv_file(self, obj):
        return f"{BASE_URL}{obj.cv_file.url}" if obj.cv_file else ""

    class Meta:
        model = JobApplicationForm
        exclude = ['id', 'is_deleted', 'date_updated']