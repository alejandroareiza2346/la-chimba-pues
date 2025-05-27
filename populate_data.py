#!/usr/bin/env python
"""
Script para poblar la base de datos con información real y completa
del sistema de gestión de aerolíneas (ARMS)
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

def clear_existing_data():
    """Limpiar datos existentes manteniendo solo los básicos"""
    print("🧹 Limpiando datos existentes...")
    
    # Marcar como eliminados los datos de prueba
    Airlines.objects.filter(name__in=['Philippine Airlines', 'Cebu Pacific', 'Air Asia Philippines']).update(delete_flag=1)
    Airport.objects.filter(name__startswith='Airport').update(delete_flag=1)
    
    print("✅ Datos de prueba limpiados")

def create_airlines():
    """Crear aerolíneas reales"""
    print("✈️ Creando aerolíneas reales...")
    
    airlines_data = [
        # Aerolíneas Colombianas
        {
            'name': 'Avianca',
            'status': '1'
        },
        {
            'name': 'LATAM Airlines Colombia',
            'status': '1'
        },
        {
            'name': 'Viva Air Colombia',
            'status': '1'
        },
        {
            'name': 'Ultra Air',
            'status': '1'
        },
        {
            'name': 'Wingo',
            'status': '1'
        },
        # Aerolíneas Internacionales
        {
            'name': 'American Airlines',
            'status': '1'
        },
        {
            'name': 'Copa Airlines',
            'status': '1'
        },
        {
            'name': 'Iberia',
            'status': '1'
        },
        {
            'name': 'Lufthansa',
            'status': '1'
        },
        {
            'name': 'Air France',
            'status': '1'
        }
    ]
    
    for airline_data in airlines_data:
        airline, created = Airlines.objects.get_or_create(
            name=airline_data['name'],
            defaults={
                'status': airline_data['status'],
                'delete_flag': 0,
                'date_added': datetime.now(),
                'date_created': datetime.now()
            }
        )
        if created:
            print(f"   ✅ Creada: {airline.name}")
        else:
            print(f"   ⚠️ Ya existe: {airline.name}")

def create_airports():
    """Crear aeropuertos reales"""
    print("🛫 Creando aeropuertos reales...")
    
    airports_data = [
        # Aeropuertos Colombianos
        {
            'name': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional José María Córdova (MDE) - Medellín',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional Rafael Núñez (CTG) - Cartagena',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional Alfonso Bonilla Aragón (CLO) - Cali',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional Ernesto Cortissoz (BAQ) - Barranquilla',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional Simón Bolívar (SMR) - Santa Marta',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional Matecaña (UIO) - Pereira',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional Gustavo Rojas Pinilla (ADZ) - San Andrés',
            'status': '1'
        },
        # Aeropuertos Internacionales
        {
            'name': 'Aeropuerto Internacional de Miami (MIA) - Estados Unidos',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional de Tocumen (PTY) - Panamá',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional de Madrid-Barajas (MAD) - España',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional Jorge Newbery Airfield (AEP) - Buenos Aires',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional José Joaquín de Olmedo (GYE) - Guayaquil',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional El Cocuy (LIM) - Lima',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional Charles de Gaulle (CDG) - París',
            'status': '1'
        },
        {
            'name': 'Aeropuerto Internacional John F. Kennedy (JFK) - Nueva York',
            'status': '1'
        }
    ]
    
    for airport_data in airports_data:
        airport, created = Airport.objects.get_or_create(
            name=airport_data['name'],
            defaults={
                'status': airport_data['status'],
                'delete_flag': 0,
                'date_added': datetime.now(),
                'date_created': datetime.now()
            }
        )
        if created:
            print(f"   ✅ Creado: {airport.name}")
        else:
            print(f"   ⚠️ Ya existe: {airport.name}")

def create_flights():
    """Crear vuelos realistas"""
    print("🛩️ Creando vuelos realistas...")
    
    # Obtener aerolíneas y aeropuertos
    airlines = list(Airlines.objects.filter(delete_flag=0))
    airports = list(Airport.objects.filter(delete_flag=0))
    
    if not airlines or not airports:
        print("❌ Error: No hay aerolíneas o aeropuertos disponibles")
        return
    
    # Definir rutas realistas
    flight_routes = [
        # Rutas Domésticas Colombia
        {
            'code': 'AV2001',
            'airline': 'Avianca',
            'from_airport': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'to_airport': 'Aeropuerto Internacional José María Córdova (MDE) - Medellín',
            'departure_hour': 6,
            'duration_hours': 1,
            'aircraft': 'A320-200'
        },
        {
            'code': 'LA4150',
            'airline': 'LATAM Airlines Colombia', 
            'from_airport': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'to_airport': 'Aeropuerto Internacional Rafael Núñez (CTG) - Cartagena',
            'departure_hour': 8,
            'duration_hours': 1.5,
            'aircraft': 'A319-100'
        },
        {
            'code': 'VV1234',
            'airline': 'Viva Air Colombia',
            'from_airport': 'Aeropuerto Internacional José María Córdova (MDE) - Medellín',
            'to_airport': 'Aeropuerto Internacional Alfonso Bonilla Aragón (CLO) - Cali',
            'departure_hour': 14,
            'duration_hours': 0.75,
            'aircraft': 'A320neo'
        },
        {
            'code': 'UX5678',
            'airline': 'Ultra Air',
            'from_airport': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'to_airport': 'Aeropuerto Internacional Ernesto Cortissoz (BAQ) - Barranquilla',
            'departure_hour': 10,
            'duration_hours': 1.25,
            'aircraft': 'B737-800'
        },
        {
            'code': 'P5990',
            'airline': 'Wingo',
            'from_airport': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'to_airport': 'Aeropuerto Internacional Gustavo Rojas Pinilla (ADZ) - San Andrés',
            'departure_hour': 12,
            'duration_hours': 2,
            'aircraft': 'B737-800'
        },
        # Rutas Internacionales
        {
            'code': 'AV019',
            'airline': 'Avianca',
            'from_airport': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'to_airport': 'Aeropuerto Internacional de Miami (MIA) - Estados Unidos',
            'departure_hour': 23,
            'duration_hours': 4.5,
            'aircraft': 'B787-8'
        },
        {
            'code': 'CM230',
            'airline': 'Copa Airlines',
            'from_airport': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'to_airport': 'Aeropuerto Internacional de Tocumen (PTY) - Panamá',
            'departure_hour': 16,
            'duration_hours': 2.5,
            'aircraft': 'B737-800'
        },
        {
            'code': 'IB6126',
            'airline': 'Iberia',
            'from_airport': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'to_airport': 'Aeropuerto Internacional de Madrid-Barajas (MAD) - España',
            'departure_hour': 1,
            'duration_hours': 9,
            'aircraft': 'A350-900'
        },
        {
            'code': 'AA958',
            'airline': 'American Airlines',
            'from_airport': 'Aeropuerto Internacional José María Córdova (MDE) - Medellín',
            'to_airport': 'Aeropuerto Internacional de Miami (MIA) - Estados Unidos',
            'departure_hour': 7,
            'duration_hours': 4.25,
            'aircraft': 'B737 MAX 8'
        },
        {
            'code': 'AF480',
            'airline': 'Air France',
            'from_airport': 'Aeropuerto Internacional El Dorado (BOG) - Bogotá',
            'to_airport': 'Aeropuerto Internacional Charles de Gaulle (CDG) - París',
            'departure_hour': 22,
            'duration_hours': 10.5,
            'aircraft': 'B777-300ER'
        }
    ]
    
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    for route in flight_routes:
        # Buscar aerolínea y aeropuertos
        try:
            airline = Airlines.objects.get(name=route['airline'], delete_flag=0)
            from_airport = Airport.objects.get(name=route['from_airport'], delete_flag=0)
            to_airport = Airport.objects.get(name=route['to_airport'], delete_flag=0)
        except (Airlines.DoesNotExist, Airport.DoesNotExist) as e:
            print(f"   ⚠️ Saltando vuelo {route['code']}: {e}")
            continue
        
        # Crear vuelos para los próximos 7 días
        for day_offset in range(7):
            flight_date = base_date + timedelta(days=day_offset)
            departure_time = flight_date + timedelta(hours=route['departure_hour'])
            arrival_time = departure_time + timedelta(hours=route['duration_hours'])
            
            flight_code = f"{route['code']}-{flight_date.strftime('%m%d')}"
            
            # Precios realistas basados en el tipo de vuelo
            if 'Internacional' in to_airport.name or 'Estados Unidos' in to_airport.name or 'España' in to_airport.name or 'París' in to_airport.name:
                # Vuelos internacionales
                economy_price = random.randint(800000, 2500000)  # COP
                business_price = economy_price * random.uniform(2.5, 4.0)
                economy_slots = random.randint(150, 200)
                business_slots = random.randint(20, 40)
            else:
                # Vuelos domésticos
                economy_price = random.randint(150000, 600000)  # COP
                business_price = economy_price * random.uniform(1.5, 2.5)
                economy_slots = random.randint(120, 180)
                business_slots = random.randint(12, 25)
            
            flight, created = Flights.objects.get_or_create(
                code=flight_code,
                defaults={
                    'airline': airline,
                    'from_airport': from_airport,
                    'to_airport': to_airport,
                    'air_craft_code': route['aircraft'],
                    'departure': departure_time,
                    'estimated_arrival': arrival_time,
                    'economy_slots': economy_slots,
                    'business_class_slots': business_slots,
                    'economy_price': int(economy_price),
                    'business_class_price': int(business_price),
                    'delete_flag': 0,
                    'date_added': datetime.now(),
                    'date_created': datetime.now()
                }
            )
            
            if created:
                print(f"   ✅ Vuelo creado: {flight_code} - {from_airport.name.split('(')[0].strip()} → {to_airport.name.split('(')[0].strip()}")

def create_reservations():
    """Crear reservas realistas"""
    print("🎫 Creando reservas realistas...")
    
    # Obtener vuelos disponibles
    flights = list(Flights.objects.filter(delete_flag=0))
    
    if not flights:
        print("❌ Error: No hay vuelos disponibles")
        return
    
    # Datos de pasajeros realistas
    passengers_data = [
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
        },
        {
            'first_name': 'Laura',
            'middle_name': 'Patricia',
            'last_name': 'Jiménez Torres',
            'gender': 'Femenino',
            'contact': '+57 318 789 0123',
            'email': 'laura.jimenez@email.com',
            'address': 'Carrera 80 #15-45, Pereira, Colombia'
        },
        {
            'first_name': 'Roberto',
            'middle_name': 'Enrique',
            'last_name': 'Vargas Díaz',
            'gender': 'Masculino',
            'contact': '+57 305 567 8901',
            'email': 'roberto.vargas@email.com',
            'address': 'Avenida Santander #67-34, Santa Marta, Colombia'
        },
        {
            'first_name': 'Claudia',
            'middle_name': 'Marcela',
            'last_name': 'Ramírez Soto',
            'gender': 'Femenino',
            'contact': '+57 312 890 1234',
            'email': 'claudia.ramirez@email.com',
            'address': 'Calle 100 #23-56, Bogotá, Colombia'
        },
        {
            'first_name': 'Fernando',
            'middle_name': 'Alejandro',
            'last_name': 'Castro Mendoza',
            'gender': 'Masculino',
            'contact': '+57 317 345 6789',
            'email': 'fernando.castro@email.com',
            'address': 'Carrera 43A #18-90, Medellín, Colombia'
        },
        {
            'first_name': 'Valentina',
            'middle_name': 'Isabel',
            'last_name': 'Ruiz Aguilar',
            'gender': 'Femenino',
            'contact': '+57 314 678 9012',
            'email': 'valentina.ruiz@email.com',
            'address': 'Calle 85 #47-21, San Andrés, Colombia'
        }
    ]
    
    # Crear reservas para diferentes vuelos
    for i, passenger in enumerate(passengers_data):
        # Seleccionar un vuelo aleatorio
        flight = random.choice(flights)
        
        # Tipo de clase (80% economy, 20% business)
        ticket_type = 'Economy' if random.random() < 0.8 else 'Business'
        
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
                'status': '1',  # Confirmada
                'date_added': datetime.now(),
                'date_created': datetime.now()
            }
        )
        
        if created:
            print(f"   ✅ Reserva creada: {passenger['first_name']} {passenger['last_name']} - Vuelo {flight.code} ({ticket_type})")

def main():
    """Función principal"""
    print("🚀 Iniciando población de datos reales para ARMS")
    print("=" * 60)
    
    try:
        clear_existing_data()
        create_airlines()
        create_airports()
        create_flights()
        create_reservations()
        
        print("\n" + "=" * 60)
        print("✅ ¡Población de datos completada exitosamente!")
        print("\n📊 RESUMEN:")
        print(f"   • Aerolíneas: {Airlines.objects.filter(delete_flag=0).count()}")
        print(f"   • Aeropuertos: {Airport.objects.filter(delete_flag=0).count()}")
        print(f"   • Vuelos: {Flights.objects.filter(delete_flag=0).count()}")
        print(f"   • Reservas: {Reservation.objects.all().count()}")
        
    except Exception as e:
        print(f"❌ Error durante la población de datos: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
