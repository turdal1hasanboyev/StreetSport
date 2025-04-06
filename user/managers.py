from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, first_name=None, last_name=None, phone_number=None, image=None, description=None, password=None, **extra_fields):
        from .models import CustomUser

        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            image=image,
            description=description,
            **extra_fields,
        )
        user.role = CustomUser.Roles.USER
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name=None, last_name=None, phone_number=None, image=None, description=None, password=None, **extra_fields):
        from .models import CustomUser
        
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            image=image,
            description=description,
            password=password,
            **extra_fields,
        )
        user.role = CustomUser.Roles.ADMIN
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
