import rotor


def encrypt(data):
	key_a = '!@#$%^&*'
	key_b = 'abcdefgh'
	key_c = '<>{}:"'

	secret = '|' + key_b + key_a + key_c + '|' + key_b + 'EOF'

	rot = rotor.newrotor(secret)
	# data = rot.encrypt('rot')


'''

secret = + + + + + + + 



key_a + '|' 


str(4) + '|' + key_b + key_a + key_c 

'''
