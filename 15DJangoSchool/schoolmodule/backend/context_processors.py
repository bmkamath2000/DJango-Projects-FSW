import os
import json
from pathlib import Path
from django.conf import settings

def static_files(request):
    manifest_path = Path(settings.BASE_DIR) / 'frontend' / 'build' / 'asset-manifest.json'
    with open(manifest_path) as f:
        manifest = json.load(f)
    return {
        'main_js': manifest['files']['main.js'],
        'main_css': manifest['files'].get('main.css', '')
    }
