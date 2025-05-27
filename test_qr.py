#!/usr/bin/env python
"""
Script de prueba para verificar que los QR codes funcionan correctamente
"""
import os
import django
from django.conf import settings

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_arms.settings')
django.setup()

from qr_code.qrcode.utils import qr_code_url_from_text # type: ignore

def test_qr_generation():
    try:
        # Probar generar un QR code simple
        test_text = "ARMS-123-TEST-RESERVATION"
        qr_url = qr_code_url_from_text(test_text, size=5, version=1, image_format='png')
        
        print("✅ QR Code generation successful!")
        print(f"Test text: {test_text}")
        print(f"Generated QR URL: {qr_url}")
        return True
    except Exception as e:
        print(f"❌ Error generating QR code: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Testing QR Code functionality...")
    print("-" * 50)
    success = test_qr_generation()
    print("-" * 50)
    if success:
        print("🎉 All QR Code tests passed!")
    else:
        print("⚠️  QR Code tests failed!")
