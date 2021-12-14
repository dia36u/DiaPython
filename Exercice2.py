#Someone Said

quote ="Lao-Tseu à dit: 'Si tu donnes un poisson à un homme, il mangera un jour. Si tu lui apprends à pêcher, il mangera toujours.'"
print(quote)

# First Name Cases

prenom = "babacar"
print(prenom)
print(prenom.title())
print(prenom.upper())

# Full Name

nom = "dia"
print(prenom + ' ' + nom)

# About This Person

prenomPerson = "lao"
nomPerson = "tseu"
citation = prenomPerson.title() + '-' + nomPerson.title() + ' à dit: \'Si tu donnes un poisson à un homme, il mangera un jour. Si tu lui apprends à pêcher, il mangera toujours.\''
print(citation)

# Name Strip

prenomWhitespace = " babacar "
print(prenomWhitespace)
print(prenomWhitespace.lstrip())
print(prenomWhitespace.rstrip())
print(prenomWhitespace.strip())