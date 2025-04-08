filename = "lyric_harderbetterfasterstronger"

decoded_file = str(open(f"text_files/decoded/{filename}_decoded").read())
to_encode_file = str(open(f"text_files/to_encode/{filename}").read())

print(decoded_file == to_encode_file)