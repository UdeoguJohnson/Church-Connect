from django.db import models

class userModel(models.Model):
    ADMIN_ROLE = 'A'
    MEMBER_ROLE = 'M'

    ROLE_CHOICES =[
        (ADMIN_ROLE, 'Admin'),
        (MEMBER_ROLE, 'Member'),
    ]

    church_name = models.ForeignKey("accounts.churchModel", 
                                           on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.EmailField(unique= True, max_length= 255)
    role = models.CharField(max_length=1, 
                            choices= ROLE_CHOICES, 
                            default=MEMBER_ROLE)
    
    def __str__(self):
       return f'{self.first_name} {self.last_name} {self.role}'
    

class eventModel(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    date = models.DateTimeField(auto_created=True)
    created_by = models.ForeignKey(userModel, 
                                   on_delete= models.CASCADE)

    def __str__(self):
       return self.title

class prayerRequestModel(models.Model):
    created_by = models.ForeignKey(userModel, 
                                   on_delete= models.CASCADE)
    title = models.CharField(max_length= 255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.description}" 
    