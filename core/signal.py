
###################Question 1#################################
from django.dispatch import Signal, receiver
import time

# Define a signal
my_signal = Signal()

# Receiver function
@receiver(my_signal)
def my_receiver(*args, **kwargs):
    print("Receiver started")
    time.sleep(2)  # Simulate a delay
    print("Receiver finished")

# Sending the signal
print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent.")


###################Question 2#################################
from django.dispatch import Signal, receiver
import threading

# Define a signal
my_signal = Signal()

# Receiver function
@receiver(my_signal)
def my_receiver(*args, **kwargs):
    print("Receiver is running in thread:", threading.current_thread().name)

# Sending the signal
print("Sending signal from thread:", threading.current_thread().name)
my_signal.send(sender=None)

###################Question 3#################################
from django.db import models, transaction
from django.dispatch import Signal, receiver
from django.db.utils import OperationalError
from .models import MyModel
# Define a signal
my_signal = Signal()

# Receiver function
@receiver(my_signal)
def my_receiver(*args, **kwargs):
    print("Receiver executed")


# Function to demonstrate transaction and signal
def create_instance():
    try:
        with transaction.atomic():
            instance = MyModel(name="Test")
            instance.save()
            my_signal.send(sender=None)
            print("Signal sent after save.")
    except OperationalError:
        print("Transaction rolled back.")

create_instance()
