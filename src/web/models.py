from django.db import models


class House(models.Model):
    name = models.CharField(help_text='T ex "Round House 1"', max_length=128)
    desc = models.TextField(help_text='T ex "This is the largest..."')
    pers_capacity = models.IntegerField(
                            help_text='Hur många kan som mest sova i ' +
                                      'huset? T ex 10')
    n_rooms = models.SmallIntegerField(help_text="Hur många rum har huset?")
    n_doubles = models.SmallIntegerField(help_text="Hur många dubbelsängar?")
    n_singles = models.SmallIntegerField(help_text="Hur många enkelsängar?")
    img_path = models.CharField(help_text="Sökvägen till bilden",
                                max_length=128)
    tripadvisor_book_link = models.URLField(
                                help_text='Länk till tripadvisors ' +
                                          'bokningssida')

    def __repr__(self):
        return 'House: {}'.format(self.name)

    def __str__(self):
        return self.__repr__()
