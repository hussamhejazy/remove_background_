from rembg import remove

def remove_background(input_path):
    output_path = 'static/uploads/output_image.png'
    with open(input_path, 'rb') as input_file:
        with open(output_path, 'wb') as output_file:
            output_file.write(remove(input_file.read()))
    return output_path
