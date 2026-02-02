#!/usr/bin/env python3
"""
Generate PWA icons for EpiskoAI app
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename):
    """Create a square icon with gradient background and shield emoji"""
    # Create image with gradient
    img = Image.new('RGB', (size, size), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Create gradient background
    for y in range(size):
        # Gradient from #1a1a2e to #4a90e2
        r = int(26 + (74 - 26) * y / size)
        g = int(26 + (144 - 26) * y / size)
        b = int(46 + (226 - 46) * y / size)
        draw.line([(0, y), (size, y)], fill=(r, g, b))
    
    # Add rounded corners
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    corner_radius = size // 5
    mask_draw.rounded_rectangle([(0, 0), (size, size)], corner_radius, fill=255)
    
    # Apply mask
    img.putalpha(mask)
    
    # Try to add text
    try:
        # Use a bold font if available
        font_size = size // 2
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        # Add "E" text
        text = "E"
        # Get text bounding box
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Center text
        x = (size - text_width) // 2
        y = (size - text_height) // 2 - font_size // 8
        
        # Draw text with shadow
        shadow_offset = max(2, size // 100)
        draw.text((x + shadow_offset, y + shadow_offset), text, fill=(0, 0, 0, 128), font=font)
        draw.text((x, y), text, fill='white', font=font)
    except Exception as e:
        print(f"Could not add text to icon: {e}")
    
    # Save the image
    img.save(filename, 'PNG')
    print(f"Created {filename}")

def main():
    # Create icons directory
    os.makedirs('icons', exist_ok=True)
    
    # Generate icons in various sizes
    sizes = [16, 32, 72, 96, 128, 144, 152, 192, 384, 512]
    
    for size in sizes:
        filename = f'icons/icon-{size}x{size}.png'
        create_icon(size, filename)
    
    print("\n✓ All icons generated successfully!")
    print("The app is ready to be installed as a PWA.")

if __name__ == '__main__':
    main()
