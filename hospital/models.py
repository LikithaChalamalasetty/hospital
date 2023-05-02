from django.db import models
from django.contrib.auth.models import User

# Create your models here.
departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists',
                'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/DoctorProfilePic/',default=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default='Cardiologist')
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='doctor/')
    details = models.TextField()
    experience = models.TextField()
    expertize = models.ManyToManyField(to='Expertize', related_name='doctors')
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    status = models.BooleanField(default=False)
    
    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department,self.name)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"

class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)


class Slider(models.Model):
    caption = models.CharField(max_length=150)
    slogan = models.CharField(max_length=120)
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.caption[:20]

    class Meta:
        verbose_name_plural = 'Slider'


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    items = models.ManyToManyField(to='Item',)
    thumbnail = models.ImageField(upload_to='services/')
    cover = models.ImageField(upload_to='services/')
    image1 = models.ImageField(upload_to='services/', blank=True, null=True)
    image2 = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Expertize(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Gallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galleries"
