# cli.py

import click
from database import session
from models import Contact

def display_menu():
    click.echo("~~Address Book Manager~~")
    click.echo("\nWhat would you like to do?\n")
    click.echo("1. Add Contact")
    click.echo("2. Edit Contact")
    click.echo("3. Delete Contact")
    click.echo("4. Search Contacts")
    click.echo("5. Exit")

def add_contact():
    name = click.prompt("Enter name")
    phone = click.prompt("Enter phone number")
    new_contact = Contact(name=name, phone_number=phone)
    session.add(new_contact)
    session.commit()
    click.echo("Contact added successfully!")

def edit_contact():
    contact_id = click.prompt("Enter contact ID to edit")
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        name = click.prompt("Enter name", default=contact.name)
        phone = click.prompt("Enter phone number", default=contact.phone_number)
        contact.name = name
        contact.phone_number = phone
        session.commit()
    else:
        click.echo("Contact not found!")

def delete_contact():
    contact_id = click.prompt("Enter contact ID to delete")
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        click.echo("Contact found! Deleting...")
        session.delete(contact)
        session.commit()
    else:
        click.echo("Contact not found!")

def search_contacts():
    search_term = click.prompt("Enter search term")
    contacts = session.query(Contact).filter(Contact.name.contains(search_term) | Contact.phone_number.contains(search_term)).all()
    if contacts:
        for contact in contacts:
            click.echo(f"Name: {contact.name} Phone: {contact.phone_number}")
    else:
        click.echo("No contacts found")

@click.command()
def cli():
    while True:
        display_menu()
        choice = click.prompt("\nEnter your choice:", type=int)

        if choice == 1:
            add_contact()
        elif choice == 2:
            edit_contact()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            search_contacts()
        elif choice == 5:
            click.echo("Exiting...")
            break

if __name__ == "__main__":
    cli()
    #
