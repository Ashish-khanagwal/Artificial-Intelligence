from abc import ABC, abstractmethod

# class EmailService:
#
#     def _connect(self):
#         print("Connecting to the email server...")
#
#     def _authenticate(self):
#         print("Authenticating.....")
#
#     def send_email(self):
#         self._connect()
#         self._authenticate()
#         print("Sending email..")
#         self._disconnect()
#
#     def _disconnect(self):
#         print("Disconnecting from the email server...")
#
#
# email = EmailService()
# email.send_email()

"""
Why it shows abstraction:
- The internal steps to send an email (connecting, authenticating, disconnecting) are hidden inside the class and are not exposed or called directly by the user.
- The user interacts with only one public method: send_email().
- This method acts as a simple interface hiding complex internal processes, fulfilling the goal of abstraction.

Why it is not complete/formal abstraction:
- The internal methods are marked with a single underscore (e.g., _connect), indicating they are "protected" by convention but not truly enforced as private or abstract.
- The example does not use Python’s abc module or abstract methods, so it’s not "formal abstraction" via abstract classes.
- It does not enforce stating any mandatory methods that subclasses must implement (if inheritance was intended).
"""

# Perfect Example


class EmailService(ABC):

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email..")
        self._disconnect()

    @abstractmethod
    def _connect(self):
        pass  # Must be implemented by subclasses

    @abstractmethod
    def _authenticate(self):
        pass  # Must be implemented by subclasses

    @abstractmethod
    def _disconnect(self):
        pass  # Must be implemented by subclasses


# Concrete subclass implementing the abstract methods
class MyEmailService(EmailService):

    def _connect(self):
        print("Connecting to the email server...")

    def _authenticate(self):
        print("Authenticating.....")

    def _disconnect(self):
        print("Disconnecting from the email server...")


# Usage
email = MyEmailService()
email.send_email()
