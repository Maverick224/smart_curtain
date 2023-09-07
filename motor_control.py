import RPi.GPIO as GPIO
import time
import sys

# Konfigurasi pin motor dan PWM
ENA = 12  # PWM pin untuk motor 1
IN1 = 17  # Kontrol arah motor 1
IN2 = 18  # Kontrol arah motor 1
ENB = 13  # PWM pin untuk motor 2
IN3 = 23  # Kontrol arah motor 2
IN4 = 24  # Kontrol arah motor 2

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Inisialisasi PWM untuk motor 1 dan motor 2
pwm_motor1 = GPIO.PWM(ENA, 25)  # Frekuensi PWM 10 Hz untuk motor 1
pwm_motor2 = GPIO.PWM(ENB, 75)  # Frekuensi PWM 10 Hz untuk motor 2

pwm_motor1.start(0)  # Mulai dengan duty cycle 0
pwm_motor2.start(0)  # Mulai dengan duty cycle 0

# Fungsi untuk menggerakkan motor 1 maju
def motor1_maju(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm_motor1.ChangeDutyCycle(speed)

# Fungsi untuk menggerakkan motor 1 mundur
def motor1_mundur(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_motor1.ChangeDutyCycle(speed)

# Fungsi untuk menggerakkan motor 2 maju
def motor2_maju(speed):
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_motor2.ChangeDutyCycle(speed)

# Fungsi untuk menggerakkan motor 2 mundur
def motor2_mundur(speed):
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_motor2.ChangeDutyCycle(speed)

# Fungsi untuk menghentikan motor 1 dan motor 2
def berhenti_motor():
    pwm_motor1.ChangeDutyCycle(0)
    pwm_motor2.ChangeDutyCycle(0)

# Menerima perintah dari baris perintah (command-line arguments)
if len(sys.argv) != 2:
    print("Gunakan: python motor_control.py [motor1/motor2]")
else:
    perintah_motor = sys.argv[1]

    if perintah_motor == "motor1":
        motor1_maju(100)  # Motor 1 maju dengan kecepatan 25%
        time.sleep(9)  # Motor 1 bergerak selama 2 detik
        berhenti_motor()  # Motor 1 berhenti
    elif perintah_motor == "motor2":
        motor2_mundur(100)  # Motor 2 maju dengan kecepatan 25%
        time.sleep(9)  # Motor 2 bergerak selama 2 detik
        berhenti_motor()  # Motor 2 berhenti

# Membersihkan GPIO
GPIO.cleanup()