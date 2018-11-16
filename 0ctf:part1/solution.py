import rotor

f = open('encrypted_flag', 'rb')

encrypted_flag = f.read()


key_a = '!@#$%^&*'
key_b = 'abcdefgh'
key_c = '<>{}:"'


secret = key_a * 4 + '|' + (key_b + key_a + key_c) * 2 + '|' + key_b*2 + 'EOF'


rt = rotor.newrotor(secret)

rot = rt.decrypt(encrypted_flag)

print 'Decrypted: '
print rot

