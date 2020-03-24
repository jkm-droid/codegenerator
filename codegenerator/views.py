from django.contrib import messages
from django.shortcuts import render, redirect
from .generatecode import generate_first_string, generate_second_string, generate_first_digit, generate_second_digit


def index_view(request):
    final_username = ""
    if request.method == 'POST':
        username = request.POST['username']

        if username == '':
            messages.error(request, 'Username cannot be empty!')
            return redirect('generatecode')
        else:
            if len(username) < 4:
                messages.error(request, 'Username must be 4 or more characters!')
                return redirect('generatecode')
            else:
                enter = username
                new_enter = enter[:-1]

                first_username = generate_first_string(enter)
                second_username = generate_second_string(enter)

                first_number = generate_first_digit()
                second_number = generate_second_digit()

                final_username = f'{new_enter}-{first_username}{first_number}-{second_username}{second_number}'

                with open('usernames.txt', 'a+') as file:
                    generated_username = f'{enter},{final_username}\n'
                    file.write(generated_username)

                print(final_username)

    template_name = 'index.html'
    context = {'final_username': final_username}

    return render(request, template_name, context)
