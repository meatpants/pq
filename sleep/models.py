from django.db import models
from sanction import Client
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

states = {1:'asleep', 2:'awake', 3:'really awake'}


def validate_sleep_state(value):
	if value not in state.keys():
		raise ValidationError(
			_('%(value)s is not a valid sleep state'),
			params={'value': value},
		)



class Sleep(models.Model):

	
	state_start = models.DateTimeField('state start')
	state = models.PositiveSmallIntegerField('sleep state', validators=[validate_sleep_state])

	def get_state(self):
		return(states[self.state])
	

	def __str__(self):
		return 'State {0} at {1}'.format(states[self.state], self.state_start)
		#return 'Foo'