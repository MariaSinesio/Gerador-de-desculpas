from django.db import models
import random

class PedidoDesculpa(models.Model):
    text = models.CharField(max_length=200)
    color = models.CharField(max_length=7, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.color:
            # Lista de cores agradáveis
            colors = [
                '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', 
                '#FFA07A', '#87CEEB', '#DDA0DD', '#98FB98',
                '#FFB6C1', '#B0C4DE', '#DEB887', '#BA55D3'
            ]
            self.color = random.choice(colors)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.text
# Create your models here.
