from django.db import models

class Customer(models.Model):
  OTHERS = 'OT'
  TRUST = 'TR'
  GOVERNMENT = 'GO'
  NON_GOVERNMENT = 'NG'
  LIMITED_COMPANY = 'LC'
  PARTNERSHIP_JOINT_VENTURE = 'PJ'

  ORGANIZATION_TYPE = [
    (OTHERS, 'Others'),
    (TRUST, 'Non Government'),
    (GOVERNMENT, 'Government'),
    (LIMITED_COMPANY, 'Limited Company'),
    (PARTNERSHIP_JOINT_VENTURE, 'Partner / Joint Venture'),
  ]

  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone = models.CharField(max_length=13, unique=True)
  email = models.EmailField(unique=True, null=True, blank=True, default="info@email.com")

  organization_type = models.CharField(max_length=2, choices=ORGANIZATION_TYPE)
  organization_name = models.CharField(max_length=20)
  
  status = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}"

  class Meta:
    ordering = ['first_name', 'last_name']


class Message(models.Model):
  ALERT_NOT_URGENT = 'NU'
  ALERT_MODERATE = 'MO'
  ALERT_URGENT = 'UR'

  ALERT_CHOICES = [
    (ALERT_NOT_URGENT, 'Not Urgent'),
    (ALERT_MODERATE, 'Moderate'),
    (ALERT_URGENT, 'Urgent'),
  ]

  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

  message = models.CharField(max_length=255)
  message_alert = models.CharField(max_length=2, choices=ALERT_CHOICES, default=ALERT_NOT_URGENT)
  
  status = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.message

  class Meta:
    ordering = ['-created_at']


class TaxRegion(models.Model):
  REGION = [

    ('AR', 'Arusha'),	
    ('DS', 'Dar es Salaam	'),
    ('DO', 'Dodoma'),
    ('GE', 'Geita'),	
    ('IR', 'Iringa'),
    ('KA', 'Kagera'),	
    ('KT', 'Katavi'),	
    ('KG', 'Kigoma'),	
    ('KI', 'Kilimanjaro'),
    ('LI', 'Lindi'),
    ('MA', 'Manyara'),		
    ('MR', 'Mara'),		
    ('MB', 'Mbeya'),		
    ('MM', 'Mjini Magharibi'),		
    ('MO', 'Morogoro'),	
    ('MT', 'Mtwara'),		
    ('MW', 'Mwanza'),	
    ('NJ', 'Njombe'),		
    ('PN', 'Pemba North Region'),	
    ('PS', 'Pemba South Region'),	
    ('PW', 'Pwani'),		
    ('RU', 'Rukwa'),	
    ('RV', 'Ruvuma'),	
    ('SH', 'Shinyanga'),	
    ('SI', 'Simiyu'),		
    ('SG', 'Singida'),		
    ('SW', 'Songwe'),	
    ('TA', 'Tabora'),		
    ('TN', 'Tanga'),		
    ('UN', 'Unguja North Region'),	
    ('US', 'Unguja South Region'),

  ]

  customer = models.OneToOneField(Customer, models.CASCADE, primary_key=True)

  region = models.CharField(max_length=2, choices=REGION)
  district = models.CharField(max_length=100)
  status = models.BooleanField(default=True)

  created_at = models.DateField(auto_now_add=True)

  def __str__(self) -> str:
    return self.region

  class Meta:
    ordering = ['region', 'district']