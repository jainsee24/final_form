from django.db import models

class UserDetail(models.Model):
    username = models.CharField(max_length=150, unique=True)
    initialPermission    = models.BooleanField(default=False)
    replacement = models.BooleanField(default=False)
    renewal = models.BooleanField(default=False)
    familyName = models.CharField(max_length=100, blank=True)
    givenName = models.CharField(max_length=100, blank=True)
    middleName = models.CharField(max_length=100, blank=True)
    otherNames_familyName_1 = models.CharField(max_length=100, blank=True)
    otherNames_givenName_1 = models.CharField(max_length=100, blank=True)
    otherNames_middleName_1 = models.CharField(max_length=100, blank=True)
    otherNames_familyName_2 = models.CharField(max_length=100, blank=True)
    otherNames_givenName_2 = models.CharField(max_length=100, blank=True)
    otherNames_middleName_2 = models.CharField(max_length=100, blank=True)
    otherNames_familyName_3 = models.CharField(max_length=100, blank=True)
    otherNames_givenName_3 = models.CharField(max_length=100, blank=True)
    otherNames_middleName_3 = models.CharField(max_length=100, blank=True)
    inCareOfName = models.CharField(max_length=100, blank=True)
    streetNumberName = models.CharField(max_length=100, blank=True)
    aptSteFlr = models.CharField(max_length=100, blank=True)
    cityOrTown = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipCode = models.CharField(max_length=100, blank=True)
    isPhysicalSameAsMailing = models.BooleanField(default=True)
    physicalStreetNumberName = models.CharField(max_length=100, blank=True)
    physicalAptSteFlr = models.CharField(max_length=100, blank=True)
    physicalCityOrTown = models.CharField(max_length=100, blank=True)
    physicalState = models.CharField(max_length=100, blank=True)
    physicalZipCode = models.CharField(max_length=100, blank=True)
    alienRegistrationNumber = models.CharField(max_length=100, blank=True)
    uscisAccountNumber = models.CharField(max_length=100, blank=True)
    hasPreviouslyFiledI765 = models.BooleanField(default=False)
    hasSSACard = models.BooleanField(default=False)
    wantsSSACard = models.BooleanField(default=False)
    wants_ssa_card = models.BooleanField(default=False)
    consentForSSADisclosure = models.BooleanField(default=False)
    fatherFamilyName = models.CharField(max_length=100, blank=True)
    fatherGivenName = models.CharField(max_length=100, blank=True)
    motherFamilyName = models.CharField(max_length=100, blank=True)
    motherGivenName = models.CharField(max_length=100, blank=True)
    countriesOfCitizenship1 = models.CharField(max_length=100, blank=True)
    countriesOfCitizenship2 = models.CharField(max_length=100, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    countryOfBirth = models.CharField(max_length=100, blank=True)
    cityOfBirth = models.CharField(max_length=100, blank=True)
    stateProvinceOfBirth = models.CharField(max_length=100, blank=True)
    immigrationStatusAtArrival = models.CharField(max_length=100, blank=True)
    currentImmigrationStatus = models.CharField(max_length=100, blank=True)
    sevisNumber = models.CharField(max_length=100, blank=True)
    employerNameEVerify = models.CharField(max_length=100, blank=True)
    employerEVerifyID = models.CharField(max_length=100, blank=True)
    eligibilityCategory = models.CharField(max_length=100, blank=True)
    travelDocumentNumber = models.CharField(max_length=100, blank=True)
    formI94Number = models.CharField(max_length=100, blank=True)
    placeOfLastArrival = models.CharField(max_length=100, blank=True)
    dateOfLastArrival = models.DateField(null=True, blank=True)  # Consider changing to DateField
    countryOfPassport = models.CharField(max_length=100, blank=True)
    passportExpirationDate = models.DateField(null=True, blank=True)  # Consider changing to DateField
    passportNumber = models.CharField(max_length=100, blank=True)
    stemOptCategory = models.CharField(max_length=100, blank=True)
    arrestedOrConvicted_1 = models.BooleanField(default=False)
    arrestedOrConvicted_2 = models.BooleanField(default=False)
    specialFilingInstructions = models.CharField(max_length=255, blank=True)
    employmentBasedCategories = models.CharField(max_length=100, blank=True)
    uscisOnlineAccountNumber = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    maritalStatus = models.CharField(max_length=50, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    h1bSpouseI797ReceiptNumber = models.CharField(max_length=100, blank=True)
    i140ReceiptNumber = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.familyName} {self.givenName}"
