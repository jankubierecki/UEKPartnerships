from django.db import models

from company import models as company_models
from university import models as university_models


class Contract(models.Model):
    contract_date = models.DateField("Data zawiązania umowy")
    amount = models.FloatField("Kwota w złotówkach", null=True, blank=True)
    contract_number = models.CharField("Numer umowy", max_length=100)
    additional_info = models.TextField("Dodatkowe Informacje")
    company = models.ForeignKey(company_models.Company, on_delete=models.CASCADE, related_name="contracts",
                                verbose_name="Firmy")
    partnership = models.OneToOneField("Partnership", on_delete=models.SET_NULL, null=True, related_name="contract",
                                       verbose_name="Współprace")
    institute_unit = models.ForeignKey(university_models.InstituteUnit, on_delete=models.CASCADE, null=True,
                                       related_name="contracts",
                                       verbose_name="Jednostki Współpracujące")

    def __str__(self):
        return "%s %s" % (self.contract_number, self.company.name)

    class Meta:
        verbose_name = "Umowa"
        verbose_name_plural = "Umowy"
        ordering = ["-contract_date"]


class Partnership(models.Model):
    company_contact_person = models.ForeignKey(company_models.CompanyContactPerson, on_delete=models.SET_NULL,
                                               null=True,
                                               related_name="partnerships", verbose_name="Osoby Do kontaktu Firmy")
    university_contact_person = models.ForeignKey(university_models.UniversityContactPerson, on_delete=models.SET_NULL,
                                                  null=True,
                                                  related_name="partnerships", verbose_name="Osoby Do kontaktu UEK")
    contract_date = models.DateField("Data rozpoczęcia współpracy")
    last_contact_date = models.DateField("Rok ostatniego kontaktu")

    def __str__(self):
        return "%s %s" % (self.contract.contract_number, self.contract.company.name)

    class Meta:
        verbose_name = "Współpraca"
        verbose_name_plural = "Współprace"
        ordering = ["-contract_date"]
