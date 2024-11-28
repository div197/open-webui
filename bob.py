import os
import shutil
from datetime import datetime

def copy_static_assets():
    # Define source image and target locations with their filenames
    source_image = 'bob.png'
    replacements = {
        'static/favicon.png': 'Favicon',
        'static/logo.png': 'Main Logo',
        'static/splash.png': 'Splash Screen',
        'static/user.png': 'User Avatar',
        'static/static/splash-dark.png': 'Dark Mode Splash',
        'static/static/splash.png': 'Static Splash',
        'backend/open_webui/static/favicon.png': 'Backend Favicon',
        'backend/open_webui/static/logo.png': 'Backend Logo',
        'backend/open_webui/static/splash.png': 'Backend Splash',
        'backend/open_webui/utils/logo.png': 'Utils Logo'
    }

    # Check if source image exists
    if not os.path.exists(source_image):
        print(f"❌ Error: Source image {source_image} not found")
        return

    print(f"\n🔄 Starting image replacement process at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Using source image: {source_image}\n")

    successful_replacements = []
    failed_replacements = []

    # Copy to each target location
    for target_path, description in replacements.items():
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            # Copy the file
            shutil.copy2(source_image, target_path)
            successful_replacements.append((target_path, description))
            print(f"✅ Successfully replaced {description} at: {target_path}")
        except Exception as e:
            failed_replacements.append((target_path, description, str(e)))
            print(f"❌ Failed to replace {description} at: {target_path}")
            print(f"   Error: {str(e)}")

    # Print summary
    print("\n📊 Replacement Summary:")
    print(f"✅ Successful replacements: {len(successful_replacements)}")
    print(f"❌ Failed replacements: {len(failed_replacements)}")

    if failed_replacements:
        print("\n⚠️ Failed Replacements Details:")
        for path, desc, error in failed_replacements:
            print(f"- {desc} ({path})")
            print(f"  Error: {error}")

    print("\n✨ Process completed!")

if __name__ == "__main__":
    copy_static_assets()