from buscaSaude.models import *


class Profile(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.IntegerField(choices=PROFILE_TYPE, default=3)
    data_nascimento = models.DateField(default=None, null=True, blank=True)

    user_image_profile = models.ImageField(null=True, blank=True)

    favoritos = models.ManyToManyField(User, blank=True, related_name="favoritos")
    especialidades = models.ManyToManyField("Especialidade")
    enderecos = models.ManyToManyField("Endereco")

    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    ## criados try/except para evitar erro no sistema caso user admin não tenha perfil
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
