from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.contrib import messages

from mcfinance.transactions.documents import Category
from mcfinance.transactions.forms.categories import CategoryForm


def category_list(request):
    return render(request, 'categories/list.html', {
        'results': Category.objects.all(),
        'section_title': _('Categories')
    })

def category_form(request, category_id=None):
    category = Category.objects(id=category_id).first() if category_id else Category()

    if request.POST:
        form = CategoryForm(request.POST)

        if form.is_valid():
            category.populate(form.cleaned_data)
            category.save()
            messages.success(request, _('Category successfully saved.'))
            return redirect('category-edit', category_id=category.id)

    else:
        form = CategoryForm(initial={
            'name': category.name,
            'description': category.description,
        })

    return render(request, 'categories/form.html', {
        'form': form,
        'section_title': _('Edit category') if category_id else _('Create category')
    })


def category_delete(request, category_id=None):
    category = Category.objects(id=category_id).first()
    if category:
        category.delete()
        messages.success(request, _('Category successfully removed.'))

    return redirect('category-list')
