import base64

encoded_data = ''

input_file = 'ssr-in.txt'
with open(input_file, 'rb') as file:
    input_str = file.read()
    print('input_str', input_str)

    output_str = base64.b64encode(input_str)
    print('output_str', output_str)

    output_file = 'ssr-out.txt'
    with open(output_file, 'wb') as file:
        file.write(output_str)