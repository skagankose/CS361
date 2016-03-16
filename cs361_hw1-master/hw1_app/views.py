from django.shortcuts import render
import string
from django.template.defaulttags import register
from django.http import HttpResponse

# We can pass list to template instead of dictionary
# but using filter is the fancy way :)
# Template filter to get value by key in dictionary
@register.filter
def get_value(dictionary, key):
    return dictionary[key]

# Function to calculate histogram
def histogram_function(request, filename, extesion):

    # Construct directory with given filename and extension
    directory = './templates/' + str(filename) + '.' + str(extesion)

    try:

        # Open and read the file
        fp = open(directory, "r")
        data = fp.read()
        words = string.split(data)

    except:

        return HttpResponse('<h1>Error!</h1><p>No such file or directory.</p>')

    # Create histogram dictionary
    histogram = {}

    # Calculate histogram
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    # Create context dictionary to pass histogram dictionary to template
    context = {'histogram': histogram}

    # Render the template with context dictionary
    return render(request, 'histogram.html', context)


# If extension is missing, user will be redirected to warning page
def histogram_function_error(request, filename):

    # Create context dictionary with provided filename
    context = {'filename': filename}

    # Render the warning page
    return render(request, 'histogram_error.html', context)



