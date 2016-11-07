# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
# Unable to inspect table 'Album'
# The error was: 'NoneType' object has no attribute 'groups'
class Album(models.Model):
    id = models.AutoField(primary_key=True, db_column='AlbumId') # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160)
    artist = models.ForeignKey("Artist", db_column='ArtistId') # Field name made lowercase.

    class Meta:
        db_table = 'Album'
    def __str__(self):
        return "%s" % self.title


class Artist(models.Model):
    artistid = models.IntegerField(db_column='ArtistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    def __str__(self):
        return self.name

    class Meta:
        #managed = False
        db_table = 'Artist'
# Unable to inspect table 'Customer'
# The error was: 'NoneType' object has no attribute 'groups'
# Unable to inspect table 'Employee'
# The error was: 'NoneType' object has no attribute 'groups'
class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_column='CustomerId') # Field name made lowercase.
    firstname = models.CharField(max_length=40, db_column='FirstName')
    lastname = models.CharField(max_length=20, db_column='LastName')
    company = models.CharField(max_length=80, db_column='Company', blank=True)
    address = models.CharField(max_length=70, db_column='Address', blank=True)
    city = models.CharField(max_length=40, db_column='City', blank=True)
    state = models.CharField(max_length=40, db_column='State', blank=True)
    country = models.CharField(max_length=40, db_column='Country', blank=True)
    postalcode = models.CharField(max_length=10, db_column='PostalCode', blank=True)
    phone = models.CharField(max_length=24, db_column='Phone', blank=True)
    fax = models.CharField(max_length=24, db_column='Fax', blank=True)
    email = models.CharField(max_length=60, db_column='Email')
    support_rep = models.ForeignKey("Employee", null=True, db_column='SupportRepId', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return "%s, %s" % (self.lastname, self.firstname)


class Employee(models.Model):
    id = models.AutoField(primary_key=True, db_column='EmployeeId') # Field name made lowercase.
    lastname = models.CharField(max_length=20, db_column='LastName')
    firstname = models.CharField(max_length=20, db_column='FirstName')
    title = models.CharField(max_length=30, db_column='Title', blank=True)
    reports_to = models.ForeignKey("Employee", null=True, db_column='ReportsTo', blank=True)
    birthdate = models.DateTimeField(null=True, db_column='BirthDate', blank=True)
    hiredate = models.DateTimeField(null=True, db_column='HireDate', blank=True)
    address = models.CharField(max_length=70, db_column='Address', blank=True)
    city = models.CharField(max_length=40, db_column='City', blank=True)
    state = models.CharField(max_length=40, db_column='State', blank=True)
    country = models.CharField(max_length=40, db_column='Country', blank=True)
    postalcode = models.CharField(max_length=10, db_column='PostalCode', blank=True)
    phone = models.CharField(max_length=24, db_column='Phone', blank=True)
    fax = models.CharField(max_length=24, db_column='Fax', blank=True)
    email = models.CharField(max_length=60, db_column='Email', blank=True)
    class Meta:
        db_table = 'Employee'
    def __str__(self):
        return "%s, %s" % (self.lastname, self.firstname)


    
class Genre(models.Model):
    genreid = models.IntegerField(db_column='GenreId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'Genre'
    def __str__(self):
        return "%s" % self.name

# Unable to inspect table 'Invoice'
# The error was: 'NoneType' object has no attribute 'groups'
# Unable to inspect table 'InvoiceLine'
# The error was: 'NoneType' object has no attribute 'groups'
class Invoice(models.Model):
    id = models.AutoField(primary_key=True, db_column='InvoiceId')
    customer = models.ForeignKey("Customer", db_column='CustomerId')
    invoicedate = models.DateTimeField(db_column='InvoiceDate')
    billingaddress = models.CharField(max_length=70, db_column='BillingAddress', blank=True)
    billingcity = models.CharField(max_length=40, db_column='BillingCity', blank=True)
    billingstate = models.CharField(max_length=40, db_column='BillingState', blank=True)
    billingcountry = models.CharField(max_length=40, db_column='BillingCountry', blank=True)
    billingpostalcode = models.CharField(max_length=10, db_column='BillingPostalCode', blank=True)
    total = models.TextField(db_column='Total')
    def __str__(self):
        return "%s: %s" % (self.id, self.customer)
    
    class Meta:
        db_table = 'Invoice'

class Invoiceline(models.Model):
    id = models.AutoField(primary_key=True, db_column='InvoiceLineId')
    invoice = models.ForeignKey("Invoice", db_column='InvoiceId')
    track = models.ForeignKey("Track", db_column='TrackId')
    unit_price = models.DecimalField(max_digits=5, db_column='UnitPrice', decimal_places=2)
    quantity = models.IntegerField(db_column='Quantity')
    class Meta:
        db_table = 'InvoiceLine'
    def __str__(self):
        return "%s/%s/%s" % (self.track, self.invoice, self.unit_price)


 
class Mediatype(models.Model):
    mediatypeid = models.IntegerField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'MediaType'
    def __str__(self):
        return "%s" % self.name

class Playlist(models.Model):
    playlistid = models.IntegerField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'Playlist'
    def __str__(self):
        return "%s" % self.name
# Unable to inspect table 'PlaylistTrack'
# The error was: 'NoneType' object has no attribute 'groups'
# Unable to inspect table 'Track'
# The error was: 'NoneType' object has no attribute 'groups'
class PlaylistTrack(models.Model):
    #id = models.AutoField(primary_key=True)
    playlist = models.ForeignKey("Playlist", db_column='PlaylistId')
    track = models.ForeignKey("Track", db_column='TrackId')
    class Meta:
        db_table = 'PlaylistTrack'
        unique_together = ('playlist', 'track')
    

 
class Track(models.Model):
    id = models.AutoField(primary_key=True, db_column='TrackId')
    playlist = models.ManyToManyField(Playlist, through=PlaylistTrack)
    name = models.CharField(max_length=200, db_column='Name')
    album = models.ForeignKey("Album", null=True, db_column='AlbumId', blank=True)
    mediatype = models.ForeignKey("MediaType", db_column='MediaTypeId')
    genre = models.ForeignKey("Genre", null=True, db_column='GenreId', blank=True)
    composer = models.CharField(max_length=220, db_column='Composer', blank=True)
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(null=True, db_column='Bytes', blank=True)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, db_column='UnitPrice')

    class Meta:
        db_table = 'Track'
    def __str__(self):
        return "%s" % self.name
  
