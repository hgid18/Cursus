# Born2BeRoot

*Este proyecto ha sido creado como parte del currículum de 42 por hgarcia2*

## Descripción

**Born2BeRoot** es un proyecto de administración de sistemas que introduce a los estudiantes en el mundo de la virtualización y la configuración de servidores. El objetivo principal es crear una máquina virtual siguiendo reglas estrictas y directrices de seguridad, implementando conceptos fundamentales de administración de sistemas como particionado, gestión de usuarios, políticas de seguridad y configuración de servicios.

Este proyecto proporciona experiencia práctica con:
- Configuración e instalación de máquinas virtuales
- Particionado de discos con LVM y volúmenes cifrados
- Políticas de contraseñas seguras y gestión de usuarios
- Configuración de firewall y gestión de puertos
- Configuración y seguridad del servicio SSH
- Configuración y monitorización de sudo
- Scripts automatizados de monitorización del sistema

## Instrucciones

### Requisitos previos
- VirtualBox o UTM (dependiendo de la arquitectura de tu sistema)
- Imagen ISO de Debian o Rocky Linux
- Al menos 8GB de espacio en disco para la máquina virtual
- RAM suficiente (mínimo 1GB recomendado)

### Instalación

1. **Descargar la ISO**
```bash
wget https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-XX.X.X-amd64-netinst.iso
```

2. **Crear la máquina virtual**
- Abrir VirtualBox/UTM
- Crear una nueva VM con las siguientes especificaciones:
- Nombre: Born2BeRoot
- Tipo: Linux
- Memoria: 1024 MB (mínimo)
- Disco: 8 GB mínimo (VDI, asignado dinámicamente)

3. **Instalar el sistema operativo**
- Montar la imagen ISO
- Seguir el asistente de instalación
- Configurar particiones LVM cifradas según los requisitos del proyecto
- Configurar usuarios y contraseñas de acuerdo con las políticas de seguridad

4. **Configuración post-instalación**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server ufw -y
```

### Ejecución

Para iniciar la máquina virtual:
1. Abrir VirtualBox/UTM
2. Seleccionar la VM Born2BeRoot
3. Hacer clic en "Iniciar"
4. Iniciar sesión con las credenciales de usuario configuradas

Para conectarse vía SSH:
```bash
ssh username@localhost -p 4242
```

Para ejecutar el script de monitorización:
```bash
sudo /usr/local/bin/monitoring.sh
```

## Descripción del proyecto

### Elección del sistema operativo: Debian

**SO elegido**: Debian 12 (Bookworm)

**Justificación**:
- **Estabilidad**: Debian es reconocido por su estabilidad sólida como una roca, lo que lo hace ideal para aprender los fundamentos de la administración de sistemas
- **Gestión de paquetes**: El gestor de paquetes APT está ampliamente documentado y es amigable para principiantes
- **Soporte comunitario**: Documentación extensa y gran comunidad para la resolución de problemas
- **Curva de aprendizaje**: Curva de aprendizaje más suave en comparación con Rocky Linux, más adecuada para administradores de sistemas primerizos

### Debian vs Rocky Linux

**Ventajas de Debian**:
- Repositorio de software masivo
- Excelente documentación
- Muy adecuado para aprender
- Flexible y versátil

**Desventajas de Debian**:
- Versiones de software más antiguas en la versión stable
- Menor enfoque en características empresariales

**Ventajas de Rocky Linux**:
- Compatibilidad con RHEL (valioso para entornos empresariales)
- Fuerte soporte empresarial
- Integración de SELinux lista para usar
- Paquetes modernos

**Desventajas de Rocky Linux**:
- Curva de aprendizaje más pronunciada
- Comunidad más pequeña en comparación con Debian
- Menos flexible para uso de escritorio

#### Políticas de seguridad

**Política de contraseñas**:
- Longitud mínima: 10 caracteres
- Mayúsculas, minúsculas y números requeridos
- Máximo 3 caracteres idénticos consecutivos
- Caducidad de contraseña: 30 días
- Días mínimos entre cambios: 2
- Advertencia antes de caducidad: 7 días

**Gestión de usuarios**:
- Creado grupo user42 para usuarios del proyecto
- Implementadas reglas estrictas de sudo con registro
- Historial de contraseñas previene reutilización de las últimas 5 contraseñas

**Configuración de sudo**:
- Intentos de autenticación limitados (3 intentos)
- Mensaje de error personalizado para autenticación fallida
- Registro de entrada/salida en `/var/log/sudo/`
- Requisito de TTY para seguridad
- Entorno PATH restringido

#### Servicios instalados

1. **SSH (OpenSSH Server)**
- Puerto: 4242 (no estándar por seguridad)
- Inicio de sesión root deshabilitado
- Autenticación por contraseña habilitada (basada en claves recomendada para producción)

2. **UFW (Uncomplicated Firewall)**
- Solo puerto 4242 abierto
- Entrante denegado por defecto
- Saliente permitido por defecto

3. **Cron**
- Ejecución automatizada del script de monitorización
- Se ejecuta cada 10 minutos
- Difunde estadísticas del sistema

### AppArmor vs SELinux

**AppArmor** (Usado en Debian):
- **Ventajas**: Fácil de entender y configurar, sobrecarga mínima del sistema, creación rápida de perfiles
- **Desventajas**: Menor control granular, basado en rutas (puede eludirse con enlaces duros)

**SELinux** (Por defecto en Rocky Linux):
- **Ventajas**: Extremadamente granular, basado en etiquetas (más seguro), estándar de la industria para entornos de alta seguridad
- **Desventajas**: Complejo de configurar, puede romper aplicaciones si no se configura adecuadamente, curva de aprendizaje pronunciada

### UFW vs firewalld


**UFW** (Uncomplicated Firewall - Usado en este proyecto):
- **Ventajas**: Sintaxis extremadamente simple, perfecto para aprender, configuración rápida
- **Desventajas**: Menos flexible para escenarios de red complejos, menos características avanzadas

**firewalld**:
- **Ventajas**: Gestión dinámica de firewall, configuración basada en zonas, soporte de reglas enriquecidas
- **Desventajas**: Más complejo para tareas simples, requiere comprender el concepto de zonas

### VirtualBox vs UTM

**VirtualBox** (Opción tradicional):
- **Ventajas**: Software maduro, documentación extensa, excelentes guest additions, multiplataforma
- **Desventajas**: Problemas de rendimiento en Apple Silicon, requiere Rosetta 2 en Macs con chip M

**UTM** (Para Apple Silicon):
- **Ventajas**: Soporte nativo ARM64, excelente rendimiento en M1/M2/M3, interfaz moderna
- **Desventajas**: Menos maduro, menos características que VirtualBox, comunidad más pequeña

## Información adicional

### Script de monitorización

El script de monitorización (`monitoring.sh`) muestra información del sistema mediante el comando wall:
- Arquitectura y versión del kernel
- Procesadores físicos y virtuales
- Uso actual de RAM y disco
- Porcentaje de carga de la CPU
- Fecha y hora del último arranque
- Estado de LVM
- Conexiones TCP activas
- Usuarios conectados
- Información de red (IP y MAC)
- Número de comandos sudo ejecutados

### Comandos de prueba

```bash
# Verificar versión del SO
cat /etc/os-release

# Verificar estado de UFW
sudo ufw status

# Verificar configuración SSH
sudo systemctl status ssh
sudo cat /etc/ssh/sshd_config | grep Port

# Verificar política de contraseñas
sudo cat /etc/login.defs | grep PASS
sudo cat /etc/pam.d/common-password

# Verificar configuración de sudo
sudo visudo
sudo cat /etc/sudoers.d/*

# Verificar configuración de LVM
lsblk
sudo lvdisplay
sudo vgdisplay

# Probar script de monitorización
sudo /usr/local/bin/monitoring.sh
```
### Script de monitorización

El script de monitorización (`monitoring.sh`) muestra información del sistema mediante el comando wall:
- Arquitectura y versión del kernel
- Procesadores físicos y virtuales
- Uso actual de RAM y disco
- Porcentaje de carga de la CPU
- Fecha y hora del último arranque
- Estado de LVM
- Conexiones TCP activas
- Usuarios conectados
- Información de red (IP y MAC)
- Número de comandos sudo ejecutados

#### Explicación detallada del script monitoring.sh

A continuación se explica línea por línea lo que muestra el script de monitorización:

**1. Arquitectura del sistema**
```bash
arch=$(uname -a)
```

**2. Procesadores físicos**
```bash
pcpu=$(grep "physical id" /proc/cpuinfo | sort | uniq | wc -l)
```

**3. Procesadores virtuales (núcleos)**
```bash
vcpu=$(grep "^processor" /proc/cpuinfo | wc -l)
```

**4. Memoria RAM disponible y uso**
```bash
fram=$(free -m | awk '$1 == "Mem:" {print $2}')
uram=$(free -m | awk '$1 == "Mem:" {print $3}')
pram=$(free | awk '$1 == "Mem:" {printf("%.2f"), $3/$2*100}')
```

**5. Disco disponible y uso**
```bash
fdisk=$(df -BG | grep '^/dev/' | grep -v '/boot$' | awk '{ft += $2} END {print ft}')
udisk=$(df -BM | grep '^/dev/' | grep -v '/boot$' | awk '{ut += $3} END {print ut}')
pdisk=$(df -BM | grep '^/dev/' | grep -v '/boot$' | awk '{ut += $3} {ft+= $2} END {printf("%d"), ut/ft*100}')
```

**6. Porcentaje de uso de CPU**
```bash
cpul=$(top -bn1 | grep '^%Cpu' | cut -c 9- | xargs | awk '{printf("%.1f%%"), $1 + $3}')
```

**7. Fecha y hora del último reinicio**
```bash
lb=$(who -b | awk '$1 == "system" {print $3 " " $4}')
```

**8. Uso de LVM**
```bash
lvmu=$(if [ $(lsblk | grep "lvm" | wc -l) -eq 0 ]; then echo no; else echo yes; fi)
```

**9. Conexiones TCP establecidas**
```bash
ctcp=$(ss -Ht state established | wc -l)
```

**10. Usuarios conectados**
```bash
ulog=$(users | wc -w)
```

**11. Dirección IP y MAC**
```bash
ip=$(hostname -I)
mac=$(ip link show | grep "ether" | awk '{print $2}')
```

**12. Número de comandos sudo ejecutados**
```bash
cmds=$(journalctl _COMM=sudo | grep COMMAND | wc -l)
```

**13. Mostrar información con wall**
```bash
wall "	#Architecture: $arch
	#CPU physical: $pcpu
	#vCPU: $vcpu
	#Memory Usage: $uram/${fram}MB ($pram%)
	#Disk Usage: $udisk/${fdisk}Gb ($pdisk%)
	#CPU load: $cpul
	#Last boot: $lb
	#LVM use: $lvmu
	#Connections TCP: $ctcp ESTABLISHED