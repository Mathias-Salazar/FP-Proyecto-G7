print()

from Funciones import *
from Productos import *
from Proveedores import *
from Clientes import *
from Ventas import *
from datetime import datetime
import random

cont_try = 0
while True: #Sistema de inicio de sesion
    user = input('Ingrese nombre usuario: ')
    passw = input('Ingrese contraseña: ')
    #usuario: Grupo#7
    #contraseña: UPN2026-1
    
    if user == 'Grupo#7' and passw == 'UPN2026-1':
        print('\nAcceso permitido.\n')
        break
    else:
        cont_try += 1
        print('\nAcceso no permitido.')
        print('Usuario o contraseña incorrecta')
        
        if cont_try < 3:
            print(f'Intentos restantes: {3 - cont_try}\n')
        else:
            print('\nSISTEMA BLOQUEADO\n')
            exit() #Este codigo cierra abruptamente el programa si se alcanza el limite de intentos


while True:
    
    while True:
        print(':::' * 6 + ' MENÚ SISTEMA ' + ':::' * 6 + '\n') #Menu principal del sistema
        print('1. Menú Ventas')
        print('2. Menú Mercadería')
        print('3. Menú Reportes')
        print('4. Menú Proveedores')
        print('5. Menú Clientes')
        print('6. Salir definitivamente del sistema\n')
        break
    
    messi = 0
    while True:
        try:
            messi = int(input('Seleccione opción: '))
            
            if messi > 0 and messi < 7:
                break
            else:
                print('Opción no valido')
        except ValueError:
            print()
    print()
    
    match(messi):
        case 1:
            while True:
                
                while True:
                    print('===' * 6 + ' MENÚ VENTAS ' + '===' * 6 + '\n') #Menu de las ventas 1.
                    print('1. Registrar Venta')
                    print('2. Salir del menú')
                    break
                
                meVen = 0
                while True:
                    try:
                        meVen = int(input('\nSeleccione opción: '))
                        
                        if meVen > 0 and meVen < 3:
                            break
                        else:
                            print('Opción no encontrada')
                    except ValueError:
                        print()
                print()
                
                if meVen == 2:
                    break
                
                TiCompra = ''
                while True:
                    TiCompra = input('Ingrese tipo de compra (BOLETA/FACTURA): ').upper()
                    
                    if TiCompra == 'BOLETA': 
                        break
                    elif TiCompra == 'FACTURA':
                        break
                    else:
                        print('Intentelo nuevamente')
                print()
                
                dniventa = 0
                dniventa = Dni(dniventa)
                Repeticua = False
                print()
                
                if RepeDNI(dniventa):
                    Repeticua = True
                
                listaProductos = []
                listaPrecioUnit = []
                listaCantidad = []
                subtotal = 0
                totalfinal = 0
                
                productoVen = ''
                marcaVen = ''
                while True:
                    while True:
                        productoVen = TipoProducto(productoVen)
                        
                        if productoVen in productos:
                            break
                        else:
                            print('El producto que ingresó no existe')
                    
                    while True:
                        marcaVen = MarcaProducto(marcaVen)
                        
                        if marcaVen in productos[productoVen]:
                            break
                        else:
                            print('La marca del producto que ingresó no existe')
                    
                    producVender = productos[productoVen][marcaVen]
                    elProducto = (productoVen + ' ' + marcaVen).title()
                    
                    cantidadVender = 0
                    if producVender['cantidad'] > 0:
                        
                        listaProductos.append(elProducto)
                        listaPrecioUnit.append(producVender['precio'])
                        
                        while True:
                            try:
                                cantidadVender = int(input('Ingrese cantidad a vender: '))
                                    
                                if cantidadVender > 0 and cantidadVender <= producVender['cantidad']:
                                    producVender['cantidad'] -= cantidadVender
                                    break
                                else:
                                    print('La cantidad a vender no puede ser mayor al stock disponible')
                            except ValueError:
                                print('No es un número')
                        
                        listaCantidad.append(cantidadVender)
                        
                        subtotal = subtotal + (producVender['precio'] * cantidadVender)
                        
                        continuar = ''
                        
                        while True:
                            continuar = input('Desea agregar otro producto? (si/no): ').lower()
                            
                            if continuar == 'si' or continuar == 'no':
                                break
                            else:
                                print('Vuelva a intentarlo')
                        
                        if continuar == 'no':
                            break
                    else:
                        print('El producto que seleccionó no tiene stock...')
                print()
                
                totalfinal = subtotal
                
                subtotalDescuento = 0
                if Repeticua == True:
                    subtotalDescuento = totalfinal * 0.20
                    totalfinal = totalfinal - subtotalDescuento
                
                bolsas = ''
                totalbolsa = 0
                while True:
                    bolsas = input('Desea agregar bolsa? (si/no): ').lower()
                    if bolsas == 'si' or bolsas == 'no':
                        break
                    else:
                        print('Vuelva a intentarlo')
                
                if bolsas == 'si':
                    print('\n1. Bolsa Pequeña:  S/. 0.20  c/u')
                    print('2. Bolsa Grande:   S/. 0.50  c/u')
                    
                    opbolsa = 0
                    while True:
                        try:
                            opbolsa = int(input('Ingrese opción: '))
                            
                            if opbolsa > 0 and opbolsa < 3:
                                break
                        except ValueError:
                            print()
                        
                    while True:
                        try:
                            cantidadbolsa = int(input('Ingrese cantidad de bolsas: '))
                                        
                            if cantidadbolsa > 0:
                                listaCantidad.append(cantidadbolsa)
                                break
                            else:
                                print('Ingrese un número mayor a cero')
                        except ValueError:
                            print()
                    
                    match(opbolsa):
                        case 1:
                            totalbolsa = cantidadbolsa * 0.20
                            listaProductos.append('Bolsa Pequeña')
                            listaPrecioUnit.append(bolsa_pequeña)
                        case 2:
                            totalbolsa = cantidadbolsa * 0.50
                            listaProductos.append('Bolsa Grande')
                            listaPrecioUnit.append(bolsa_grande)
                    
                    subtotal += totalbolsa
                    totalfinal += totalbolsa
                
                print(f'\nMonto total: {totalfinal:.2f}')
                
                metodoPago = ''
                print('\n* Tarjeta Debito')
                print('* Tarjeta Credito')
                print('* Yape')
                print('* Efectivo\n')
                
                while True:
                    metodoPago = input('Ingrese metodo de pago: ').title()
                    
                    if metodoPago == 'Tarjeta Debito' or metodoPago == 'Tarjeta Credito' or metodoPago == 'Yape' or metodoPago == 'Efectivo':
                        break
                    else:
                        print('Metodo no encontrado')
                print()
                
                cuotapago = 0
                if metodoPago == 'Tarjeta Credito':
                    while True:
                        try:
                            cuotapago = int(input('Ingrese cantidad de cuotas: '))
                            
                            if cuotapago > 0:
                                break
                            else:
                                print('Intentelo otra vez')
                        except ValueError:
                            print()
                
                montoPagoEF = 0
                if metodoPago == 'Efectivo':
                    while True:
                        try:
                            montoPagoEF = float(input('Ingrese cantidad a pagar: '))
                            
                            if montoPagoEF > 0 and montoPagoEF >= totalfinal:
                                break
                            else:
                                print('Intentelo otra vez')
                        except ValueError:
                            print()
                print()
                
                ahora = datetime.now()

                fechaActual = ahora.strftime("%d/%m/%Y")
                horaActual = ahora.strftime("%H:%M:%S")
                
                numeramdon = 0
                while True:
                    numeramdon = random.randint(1000000, 9999999)
                    break

                codigoVenta = f'FA2026-{numeramdon}'
                
                #DETALLE DE LA COMPRA--
                
                print('\n' + '—' * 56)
                print('     ' * 4 + ' DETALLE COMPRA ' + '     ' * 4)
                print('     ' * 4 + f' {codigoVenta}' + '     ' * 4)
                print()
                
                if TiCompra == 'BOLETA':
                    print(f'\nTipo de Compra  : {TiCompra}  ' + ' ' * 12 + f'Fecha : {fechaActual}')
                elif TiCompra == 'FACTURA':
                    print(f'\nTipo de Compra  : {TiCompra} ' + ' ' * 12 + f'Fecha : {fechaActual}')
                    
                print(f'DNI del CLiente : {dniventa}' + ' ' * 12 + f'Hora  : {horaActual}')
                
                print()
                
                for i in range(len(listaProductos)):
                    
                    print(f'{listaProductos[i]}')
                    print(f'P:    {listaPrecioUnit[i]:.2f}     X     {listaCantidad[i]}' + '  ' * 13 + f'{(listaPrecioUnit[i] * listaCantidad[i]):.2f}')
                    
                    i += 1
                
                print(f'\n*** Subtotal:      S/.{subtotal:.2f}')
                if Repeticua == True:
                    print(f'*** Descuento:     S/.{subtotalDescuento:.2f}')
                print(f'*** Total Final:   S/.{totalfinal:.2f}')
                
                if metodoPago == 'Efectivo':
                    print(f'\n*** {metodoPago}       S/.{montoPagoEF:.2f}')
                    print(f'*** Vuelto:       S/.{(montoPagoEF - totalfinal):.2f}')
                elif metodoPago == 'Tarjeta Credito':
                    print(f'\n*** {metodoPago}       {cuotapago} cuota(s)')
                else:
                    print(f'\n*** {metodoPago}')
                
                print()
                print('—' * 56)
                print('\n' + '    ' * 4 + ' GRACIAS POR SU COMPRA' + '    ' * 4 + '\n')
                print('—' * 56)
                print()
                
                ReportesVentasTotal['junio']['semana 4']['miercoles'][codigoVenta] = {
                    'dni': dniventa,
                    'fecha': fechaActual,
                    'hora': horaActual,
                    'total': round(totalfinal, 2),
                    'pago': metodoPago
                }
        case 2:
            while True:
                
                while True:
                    print('===' * 6 + ' MENÚ MERCADERÍA ' + '===' * 6 + '\n') #Menu de la mercadería 2.
                    print('1. Consultar stock')
                    print('2. Agregar stock')
                    print('3. Reducir stock (daño)')
                    print('4. Salir del menú')
                    break
                
                meMerc = 0
                while True:
                    try:
                        meMerc = int(input('\nSeleccione opción: '))
                        
                        if meMerc > 0 and meMerc < 5:
                            break
                        else:
                            print('Opción no encontrada')
                    except ValueError:
                        print()
                print()
                
                if meMerc == 4: 
                    break
                
                #las tres primeras opciones comparten casi lo mismo
                tipomerc = ''
                while True:
                    tipomerc = TipoProducto(tipomerc) 
                    
                    if tipomerc in productos:
                        break
                    else:
                        print('Tipo de producto no encontrado')
                
                nomarc = ''
                while True:
                    nomarc = MarcaProducto(nomarc)
                    
                    if nomarc in productos[tipomerc]:
                        break
                    else:
                        print('Tipo de producto no encontrado')
                
                product = productos[tipomerc][nomarc]
                
                match(meMerc):
                    case 1:
                        print('\nDetalle:')
                        print(f'{tipomerc.upper()} {nomarc.upper()} / Precio: {product['precio']} | Cantidad: {product['cantidad']} /\n')
                    case 2:
                        agregar = 0
                        while True:
                            try:
                                agregar = int(input('Cantidad a agregar: '))
                                
                                if agregar > 0:
                                    break
                                else:
                                    print('ingrese un número mayor a cero')
                            except:
                                print('No es un número...')
                        print()
                        
                        print('Stock actualizado:')
                        print('Antes:')
                        print(f'{tipomerc.upper()} {nomarc.upper()} | Cantidad: {product['cantidad']}')
                        product['cantidad'] += agregar
                        print('Despues:')
                        print(f'{tipomerc.upper()} {nomarc.upper()} | Cantidad: {product['cantidad']}\n')
                    case 3:
                        if product['cantidad'] > 0:
                            disminuir = 0
                            while True:
                                try:
                                    disminuir = int(input('Cantidad a disminuir: '))
                                    
                                    if disminuir > 0:
                                        if disminuir > product['cantidad']:
                                            print('No hay suficiente stock')
                                        else:
                                            break
                                    else:
                                        print('ingrese un número mayor a cero')
                                except:
                                    print('No es un número...')
                            print()
                            
                            print('Stock actualizado:')
                            print('Antes:')
                            print(f'{tipomerc.upper()} {nomarc.upper()} | Cantidad: {product['cantidad']}')
                            product['cantidad'] -= disminuir
                            print('Despues:')
                            print(f'{tipomerc.upper()} {nomarc.upper()} | Cantidad: {product['cantidad']}\n')
                        else:
                            print('El producto no tiene stock, no se puede reducir\n')
        case 3:
            while True:
            
                while True:
                
                    print('===' * 6 + ' MENÚ REPORTES ' + '===' * 6 + '\n') #Menu de los reportes 3.
                    print('1. Ver ventas de hoy')
                    print('2. Ver ventas de la semana')
                    print('3. Ver ventas del mes')
                    print('4. Salir del menú')
                    break
                
                meRep = 0
                while True:
                    try:
                        meRep = int(input('\nSeleccione opción: '))
                        
                        if meRep > 0 and meRep < 5:
                            break
                        else:
                            print('Opción no encontrada')
                    except ValueError:
                        print()
                print()
                
                match(meRep):
                    case 1:
                        ventasHoy = ReportesVentasTotal['junio']['semana 4']['miercoles']
                        
                        print('REPORTE DE HOY\n')
                        
                        if len(ventasHoy) == 0:
                            print('No se realizó ninguna venta hoy.\n')
                        else:
                            for codigo, detalle in ventasHoy.items():
                                print(f'Codigo Compra: {codigo}')
                                print(f'DNI: {detalle['dni']}')
                                print(f'Fecha: {detalle['fecha']}')
                                print(f'Hora: {detalle['hora']}')
                                print(f'Total: S/.{detalle["total"]:.2f}\n')
                    case 2:
                        print('1. Semana 1')
                        print('2. Semana 2')
                        print('3. Semana 3')
                        print('4. Semana 4\n')
                        
                        opSema = 0
                        while True:
                            try:
                                opSema = int(input('Ingrese semana (1,2,3,4): '))
                                
                                if opSema > 0 and opSema < 5:
                                    break
                                else:
                                    print('Opción no encontrada')
                            except ValueError:
                                print()
                        print()
                        
                        semanaElegida = ReportesVentasTotal['junio'][f'semana {opSema}']
                        
                        print(f'REPORTE SEMANA {opSema}')
                        for dia, ventas in semanaElegida.items():
                            print(f'\n{dia.upper()}')
                            for codigo, detalle in ventas.items():
                                print(f'Codigo Compra: {codigo}')
                                print(f'DNI: {detalle['dni']}')
                                print(f'Fecha: {detalle['fecha']}')
                                print(f'Hora: {detalle['hora']}')
                                print(f'Total: S/.{detalle["total"]:.2f}\n')
                    case 3:
                        for semana, dias, in ReportesVentasTotal['junio'].items():
                            print(f'{semana.upper()}\n')
                            
                            for dia, ventas in dias.items():
                                print(f'{dia.upper()}\n')
                                
                                for codigo, detalle in ventas.items():
                                    print(f'Codigo Compra: {codigo}')
                                    print(f'DNI: {detalle['dni']}')
                                    print(f'Fecha: {detalle['fecha']}')
                                    print(f'Hora: {detalle['hora']}')
                                    print(f'Total: S/.{detalle['total']:.2f}\n')
                    case 4:
                        break
        case 4:
            while True:
            
                while True:
                    print('===' * 6 + ' MENÚ PROVEEDORES ' + '===' * 6 + '\n') #Menu de los proveedores 4.
                    print('1. Registro de proveedor (actualizar)')
                    print('2. Lista de Proveedores')
                    print('3. Salir del menú')
                    break
                
                mePro = 0
                while True:
                    try:
                        mePro = int(input('\nSeleccione opción: '))
                        
                        if mePro > 0 and mePro < 4:
                            break
                        else:
                            print('Opción no encontrada')
                    except ValueError:
                        print()
                print()
                
                match(mePro):
                    case 1:
                        nomProve = input('Ingrese nombre del proveedor: ').lower()
                        direccion = input('Ingrese dirección (calle, distrito): ').title()
                        telefono = 0
                        
                        while True:
                            try:
                                telefono = int(input('Ingrese telefono del proveedor: '))
                                
                                if telefono >= 900000000 and telefono <= 999999999:
                                    repetido = False
                                    telefono = str(telefono)
                                    
                                    for nombre, datos in proveedores.items():
                                        if datos['telefono'] == telefono:
                                            repetido = True
                                    
                                    if repetido == False:
                                        break
                                    else:
                                        print('El número de telefono ya existe')
                                else:
                                    print('Intentelo denuevo')
                            except ValueError:
                                print()
                        
                        correo = input('Ingrese correo del proveedor: ')
                        
                        proveedores[nomProve] = {
                            'direccion': direccion,
                            'telefono': telefono,
                            'correo': correo
                        }
                        print('Proveedor agregado correctamente\n')
                    case 2:
                        for nombre, datos in proveedores.items():
                            print(f"Proveedor: {nombre.upper()}")
                            print(f"  Dirección: {datos['direccion']}")
                            print(f"  Teléfono: {datos['telefono']}")
                            print(f"  Correo: {datos['correo']}")
                            print("-" * 50)
                        print()
                    case 3:
                        break
        case 5:
            while True:
                while True:
                    print('===' * 6 + ' MENÚ CLIENTES ' + '===' * 6 + '\n') #Menu de los clientes 5.
                    print('1. Registro de cliente')
                    print('2. Buscar cliente')
                    print('3. Lista de clientes')
                    print('4. Ver historial de compras cliente')
                    print('5. Salir del menú')
                    break
                
                meCli = 0
                while True:
                    try:
                        meCli = int(input('\nSeleccione opción: '))
                            
                        if meCli > 0 and meCli < 6:
                            break
                        else:
                            print('Opción no encontrada')
                    except ValueError:
                            print()
                print()
                
                match(meCli):
                    case 1:
                        dnicli = 0
                        
                        while True:
                            dnicli = Dni(dnicli)
                            
                            if not RepeDNI(dnicli):
                                break
                            else:
                                print('DNI ya existe')
                        
                        nomCli = input('Ingrese nombre del cliente (nombre y apellido): ').title()
                        
                        telecli = 0
                        
                        while True:
                            try:
                                telecli = int(input('Ingrese telefono del cliente: '))
                                    
                                if telecli >= 900000000 and telecli <= 999999999:
                                    telecli = str(telecli)
                                    break
                                else:
                                    print('Intentelo denuevo')
                            except ValueError:
                                print()
                        
                        correCli = input('Ingrese correo del cliente: ')
                        
                        clientes[dnicli] = {
                            'nombre': nomCli,
                            'telefono': telecli,
                            'correo': correCli
                        }
                        print('Cliente agregado correctamente\n')
                    case 2:
                        busqdni = 0
                        
                        while True:
                            busqdni = Dni(busqdni)
                            
                            if RepeDNI(busqdni):
                                break
                            else:
                                print('DNI no existe')
                        
                        Encontrado = clientes[busqdni]
                        
                        print(f'\nNombre: {Encontrado['nombre']}')
                        print(f'Telefono: {Encontrado['telefono']}')
                        print(f'Correo: {Encontrado['correo']}\n')
                    case 3:
                        for nombre, datos in clientes.items():
                            print(f"DNI: {nombre.upper()}")
                            print(f"  Nombre: {datos['nombre']}")
                            print(f"  Teléfono: {datos['telefono']}")
                            print(f"  Correo: {datos['correo']}")
                            print("-" * 50)
                        print()  
                    case 4:
                        dniBuscar = 0
                        
                        while True:
                            dniBuscar = Dni(dniBuscar)
                            
                            if RepeDNI(dniBuscar):
                                break
                            else:
                                print('DNI no existe')
                        
                        sEncontro = False
                        
                        for semana in ReportesVentasTotal['junio'].values():
                            for dia in semana.values():
                                for codigo, venta in dia.items():
                                    if venta['dni'] == dniBuscar:

                                        sEncontro = True

                                        print(f'\nCódigo: {codigo}')
                                        print(f'Fecha: {venta["fecha"]}')
                                        print(f'Hora: {venta["hora"]}')
                                        print(f'Total: S/. {venta["total"]:.2f}')
                                        print(f'Pago: {venta["pago"]}')
                                        print('-' * 30)

                        if sEncontro == False:
                            print('El cliente no tiene compras registradas.')
                        print()
                    case 5:
                        break
        case 6:
            break
print()