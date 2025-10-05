from string_utils import StringUtils
tekst = StringUtils()

# Удаление пробелов в начале

probel = tekst.trim(" Nachalo")
assert probel == "Nachalo"

probel = tekst.trim("  Nachalo")
assert probel == "Nachalo"

probel = tekst.trim(" Ivan Ivanovich")
assert probel == "Ivan Ivanovich"

probel = tekst.trim("Derizhabl")
assert probel == "Derizhabl"

probel = tekst.trim("1Derizhabl")
assert probel == "1Derizhabl"

probel = tekst.trim(" ")
assert probel == ""

# На большую букву

zagl = tekst.capitalize("petr")
assert zagl == "Petr"

zagl = tekst.capitalize(" petr")
assert zagl == " petr"

zagl = tekst.capitalize("123")
assert zagl == "123"

zagl = tekst.capitalize("")
assert zagl == ""

# Подстрока в строке

iskoma = tekst.contains("A muha tozhe vertolet", "let")
assert iskoma

iskoma = tekst.contains("Ah uehala ona", "Hala")
assert not iskoma

iskoma = tekst.contains("хор", "xop")
assert not iskoma

iskoma = tekst.contains(None, "луч")
assert not iskoma

# Удаление

udal = tekst.delete_symbol("glavnokomaduyshij Petr", "Petr")
assert udal == "glavnokomaduyshij "

udal = tekst.delete_symbol("bronetransporter", "r")
assert udal == "bonetanspote"

udal = tekst.delete_symbol("Polet", None)
assert udal == "Polet"
