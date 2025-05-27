#!/usr/bin/env python
"""
Script simplificado para poblar la base de datos con información real
"""

import os
import sys
import django
from datetime import datetime, timedelta
import random

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_arms.settings')
django.setup()

from armsApp.models import Airlines, Airport, Flights, Reservation

def create_airlines():
    """Crear aerolíneas reales"""
    print("✈️ Creando aerolíneas reales...")
    
    airlines = [
        'Avianca',
        'LATAM Airlines Colombia', 
        'Viva Air Colombia',
        'Ultra Air',
        'Wingo',
        'American Airlines',
        'Copa Airlines',
        'Iberia',
        'Lufthansa',
        'Air France'
    ]
    
    for name in airlines:
        airline, created = Airlines.objects.get_or_create(
            name=name,
            defaults={
                'status': '1',
                'delete_flag': 0,
                'date_added': datetime.now(),
                'date_created': datetime.now()
            }
        )
        if created:
            print(f"   ✅ Creada: {airline.name}")

def create_airports():
    """Crear aeropuertos reales"""
    print("🛫 Creando aeropuertos reales...")
    
    airports = [
        'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
        'Aeropuerto Internacional José María Córdova (MDE) - Medellín',
        'Aeropuerto Internacional Rafael Núñez (CTG) - Cartagena',
        'Aeropuerto Internacional Alfonso Bonilla Aragón (CLO) - Cali',
        'Aeropuerto Internacional Ernesto Cortissoz (BAQ) - Barranquilla',
        'Aeropuerto Internacional Simón Bolívar (SMR) - Santa Marta',
        'Aeropuerto Internacional Matecaña (UIO) - Pereira',
        'Aeropuerto Internacional Gustavo Rojas Pinilla (ADZ) - San Andrés',
        'Aeropuerto Internacional de Miami (MIA) - Estados Unidos',
        'Aeropuerto Internacional de Tocumen (PTY) - Panamá',
        'Aeropuerto Internacional de Madrid-Barajas (MAD) - España',
        'Aeropuerto Internacional Jorge Newbery Airfield (AEP) - Buenos Aires',
        'Aeropuerto Internacional José Joaquín de Olmedo (GYE) - Guayaquil',
        'Aeropuerto Internacional El Cocuy (LIM) - Lima',
        'Aeropuerto Internacional Charles de Gaulle (CDG) - París',
        'Aeropuerto Internacional John F. Kennedy (JFK) - Nueva York'
    ]
    
    for name in airports:
        airport, created = Airport.objects.get_or_create(
            name=name,
            defaults={
                'status': '1',
                'delete_flag': 0,
                'date_added': datetime.now(),
                'date_created': datetime.now()
            }
        )
        if created:
            print(f"   ✅ Creado: {airport.name}")

def create_flights():
    """Crear vuelos realistas"""
    print("🛩️ Creando vuelos realistas...")
    
    # Obtener todas las aerolíneas y aeropuertos
    avianca = Airlines.objects.get(name='Avianca')
    latam = Airlines.objects.get(name='LATAM Airlines Colombia')
    viva = Airlines.objects.get(name='Viva Air Colombia')
    copa = Airlines.objects.get(name='Copa Airlines')
    
    bog = Airport.objects.get(name__contains='El Dorado (BOG)')
    mde = Airport.objects.get(name__contains='José María Córdova (MDE)')
    ctg = Airport.objects.get(name__contains='Rafael Núñez (CTG)')
    clo = Airport.objects.get(name__contains='Alfonso Bonilla Aragón (CLO)')
    mia = Airport.objects.get(name__contains='Miami (MIA)')
    pty = Airport.objects.get(name__contains='Tocumen (PTY)')
    
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    flights_data = [
        {
            'code': 'AV2001',
            'airline': avianca,
            'from_airport': bog,
            'to_airport': mde,
            'departure_hour': 6,
            'duration': 1,
            'aircraft': 'A320-200',
            'economy_price': 250000,
            'business_price': 400000
        },
        {
            'code': 'LA4150',
            'airline': latam,
            'from_airport': bog,
            'to_airport': ctg,
            'departure_hour': 8,
            'duration': 1.5,
            'aircraft': 'A319-100',
            'economy_price': 300000,
            'business_price': 500000
        },
        {
            'code': 'VV1234',
            'airline': viva,
            'from_airport': mde,
            'to_airport': clo,
            'departure_hour': 14,
            'duration': 0.75,
            'aircraft': 'A320neo',
            'economy_price': 200000,
            'business_price': 350000
        },
        {
            'code': 'AV019',
            'airline': avianca,
            'from_airport': bog,
            'to_airport': mia,
            'departure_hour': 23,
            'duration': 4.5,
            'aircraft': 'B787-8',
            'economy_price': 1200000,
            'business_price': 3500000
        },
        {
            'code': 'CM230',
            'airline': copa,
            'from_airport': bog,
            'to_airport': pty,
            'departure_hour': 16,
            'duration': 2.5,
            'aircraft': 'B737-800',
            'economy_price': 800000,
            'business_price': 1500000
        }
    ]
    
    for flight_data in flights_data:
        # Crear vuelos para los próximos 3 días
        for day_offset in range(3):
            flight_date = base_date + timedelta(days=day_offset)
            departure_time = flight_date + timedelta(hours=flight_data['departure_hour'])
            arrival_time = departure_time + timedelta(hours=flight_data['duration'])
            
            flight_code = f"{flight_data['code']}-{flight_date.strftime('%m%d')}"
            
            flight, created = Flights.objects.get_or_create(
                code=flight_code,
                defaults={
                    'airline': flight_data['airline'],
                    'from_airport': flight_data['from_airport'],
                    'to_airport': flight_data['to_airport'],
                    'air_craft_code': flight_data['aircraft'],
                    'departure': departure_time,
                    'estimated_arrival': arrival_time,
                    'economy_slots': 150,
                    'business_class_slots': 20,
                    'economy_price': flight_data['economy_price'],
                    'business_class_price': flight_data['business_price'],
                    'delete_flag': 0,
                    'date_added': datetime.now(),
                    'date_created': datetime.now()
                }
            )
            
            if created:
                origin = flight_data['from_airport'].name.split('(')[0].strip()
                dest = flight_data['to_airport'].name.split('(')[0].strip()
                print(f"   ✅ Vuelo creado: {flight_code} - {origin} → {dest}")

def create_reservations():
    """Crear reservas realistas"""
    print("🎫 Creando reservas realistas...")
    
    passengers = [
        {
            'first_name': 'Carlos',
            'middle_name': 'Andrés', 
            'last_name': 'González Martínez',
            'gender': 'Masculino',
            'contact': '+57 300 123 4567',
            'email': 'carlos.gonzalez@email.com',
            'address': 'Carrera 15 #45-67, Bogotá, Colombia'
        },
        {
            'first_name': 'María',
            'middle_name': 'Elena',
            'last_name': 'Rodríguez López', 
            'gender': 'Femenino',
            'contact': '+57 310 987 6543',
            'email': 'maria.rodriguez@email.com',
            'address': 'Calle 70 #25-30, Medellín, Colombia'
        },
        {
            'first_name': 'José',
            'middle_name': 'Luis',
            'last_name': 'Hernández Silva',
            'gender': 'Masculino', 
            'contact': '+57 320 456 7890',
            'email': 'jose.hernandez@email.com',
            'address': 'Avenida El Dorado #35-12, Cartagena, Colombia'
        },
        {
            'first_name': 'Ana',
            'middle_name': 'Sofía',
            'last_name': 'Pérez Gómez',
            'gender': 'Femenino',
            'contact': '+57 315 234 5678', 
            'email': 'ana.perez@email.com',
            'address': 'Carrera 5 #12-89, Cali, Colombia'
        },
        {
            'first_name': 'Diego',
            'middle_name': 'Alberto',
            'last_name': 'Morales Cruz',
            'gender': 'Masculino',
            'contact': '+57 301 654 3210',
            'email': 'diego.morales@email.com', 
            'address': 'Calle 45 #78-23, Barranquilla, Colombia'
        }
    ]
    
    flights = list(Flights.objects.filter(delete_flag=0))
    
    for i, passenger in enumerate(passengers):
        if i < len(flights):
            flight = flights[i]
            ticket_type = 'Economy' if i % 3 != 0 else 'Business'
            
            reservation, created = Reservation.objects.get_or_create(
                flight=flight,
                first_name=passenger['first_name'],
                last_name=passenger['last_name'],
                defaults={
                    'type': ticket_type,
                    'middle_name': passenger['middle_name'],
                    'gender': passenger['gender'],
                    'contact': passenger['contact'],
                    'email': passenger['email'],
                    'address': passenger['address'],
                    'status': '1',
                    'date_added': datetime.now(),
                    'date_created': datetime.now()
                }
            )
            
            if created:
                print(f"   ✅ Reserva: {passenger['first_name']} {passenger['last_name']} - {flight.code} ({ticket_type})")

def main():
    print("🚀 Poblando base de datos con información real")
    print("=" * 50)
    
    # Marcar datos de prueba como eliminados
    Airlines.objects.filter(name__in=['Philippine Airlines', 'Cebu Pacific', 'Air Asia Philippines']).update(delete_flag=1)
    Airport.objects.filter(name__startswith='Airport').update(delete_flag=1)
    
    create_airlines()
    create_airports() 
    create_flights()
    create_reservations()
    
    print("\n" + "=" * 50)
    print("✅ Población completada!")
    print(f"📊 Aerolíneas: {Airlines.objects.filter(delete_flag=0).count()}")
    print(f"📊 Aeropuertos: {Airport.objects.filter(delete_flag=0).count()}")
    print(f"📊 Vuelos: {Flights.objects.filter(delete_flag=0).count()}")
    print(f"📊 Reservas: {Reservation.objects.all().count()}")

if __name__ == "__main__":
    main()
