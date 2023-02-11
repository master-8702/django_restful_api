from django.db import models

class Registrant(models.Model):
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    grand_father_name = models.CharField(max_length=20)
    DOB = models.DateField()  ## date of birth
    POB = models.CharField(max_length=20, help_text='place of birth')   ## place of birth
    address = models.CharField(max_length=50)
    id_card = models.FileField(upload_to='uploadedId')
    attachement = models.FileField(upload_to='uploadedAttachements')
    other_notes = models.CharField(max_length=500)

    # List of fields to display in django admin
    list_display = ['id', 'father_name','name', 'id_card']


    # Tf you want django admin to show the search bar, just add this line
    search_fields = ['name', 'fatherName']

    # To define model data list ordering
    ordering = ('id','name')

    # To decide what will be retured if Registrant object is called (used)
    def __str__(self) :
        return str(self.id)+ ' ' + self.name + ' ' + self.father_name


