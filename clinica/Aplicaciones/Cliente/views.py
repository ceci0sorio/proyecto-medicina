from django.shortcuts import render, redirect
from .models import Paciente, Empleado, Consulta

# Create your views here.

#PAGINA PRINCIPAL
def home(request):
    return render(request, "base.html")

#DATOS DEL PACIENTE
def agregarPaciente(request):
    listaPacientes= Paciente.objects.all()
    return render(request, "agregarPacientes.html", {"listaPaciente":listaPacientes})

def registrarPaciente(request):
    try:
        codigo = request.POST['txtcodigo']
        nombre = request.POST['txtnombre']
        sexo = request.POST['txtsexo']

        pacientes = Paciente.objects.create(codigo=codigo, nombre=nombre, sexo=sexo)
        return redirect('agregarPaciente')
    except:
        return redirect('agregarPaciente')

def editarPaciente(request, codigo):
    pacientes = Paciente.objects.get(codigo=codigo)
    return render(request, "edicionPaciente.html", {"Pacientes": pacientes})

def edicionPaciente(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']

    paciente = Paciente.objects.get(codigo=codigo)
    paciente.nombre=nombre
    paciente.sexo=sexo
    paciente.save()
    return redirect('agregarPaciente')

def eliminarPaciente(request, codigo):
    paciente = Paciente.objects.get(codigo=codigo)
    paciente.delete()
    return redirect('agregarPaciente')

#DATOS DEL EMPLEADO
def agregarEmpleado(request):
    listaEmpleados= Empleado.objects.all()
    return render(request, "agregarEmpleado.html", {"listaEmpleados":listaEmpleados})

def registrarEmpleado(request):
    try:
        codigo = request.POST['txtcodigo']
        nombre = request.POST['txtnombre']
        sexo = request.POST['txtsexo']
        edad = request.POST['txtedad']
        profesion = request.POST['txtprofesion']
        empleados = Empleado.objects.create(codigo=codigo, nombre=nombre, sexo=sexo, edad=edad,  profesion=profesion)
        return redirect('agregarEmpleado')
    except:
        return redirect('agregarEmpleado')

def editarEmpleado(request, codigo):
    empleados =Empleado.objects.get(codigo=codigo)
    return render(request, "edicionPaciente.html", {"Empleados": empleados})

def edicionEmpleado(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']
    edad = request.POST['txtedad']
    profesion = request.POST['txtprofesion']

    empleado = Empleado.objects.get(codigo=codigo)
    empleado.nombre=nombre
    empleado.sexo=sexo
    empleado.edad=edad
    empleado.profesion=profesion
    empleado.save()
    return redirect('agregarEmpleado')

def eliminarEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.delete()
    return redirect('agregarEmpleado')

#DATOS DEL EMPLEADO
def agregarConsulta(request):
    listaConsultas= Consulta.objects.all()
    return render(request, "agregarConsulta.html", {"listaConsultas":listaConsultas})

def registrarConsulta(request):
    try:
        codigo = request.POST['txtcodigo']
        nombre = request.POST['txtnombre']
        sexo = request.POST['txtsexo']
        edad = request.POST['txtedad']
        especialidad = request.POST['txtespecialidad']
        motivo = request.POST['txtmotivo']

        consultas = Consulta.objects.create(codigo=codigo, nombre=nombre, sexo=sexo, edad=edad,   especialidad=especialidad, motivo=motivo)
        return redirect('agregarConsulta')
    except:
        return redirect('agregarConsulta')

def editarConsulta(request, codigo):
    consultas =Consulta.objects.get(codigo=codigo)
    return render(request, "edicionConsulta.html", {"Consultas": consultas})

def edicionConsulta(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']
    edad = request.POST['txtedad']
    especialidad = request.POST['txtespecialidad']
    motivo = request.POST['txtmotivo']

    consulta = Consulta.objects.get(codigo=codigo)
    consulta.nombre=nombre
    consulta.sexo=sexo
    consulta.edad=edad
    consulta.especialidad=especialidad
    consulta.motivo=motivo
    consulta.save()
    return redirect('agregarConsulta')

def eliminarConsulta(request, codigo):
    consulta = Consulta.objects.get(codigo=codigo)
    consulta.delete()
    return redirect('agregarConsulta')
       