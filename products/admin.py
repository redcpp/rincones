from django.contrib import admin

from .models import Product, ProductImage, Category

class ProductImageInline(admin.TabularInline):
      model = ProductImage
      min_num = 1
      max_num = 20
      extra = 1

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ('title', 'description')
    list_display = ('title', 'price', 'active', 'updated')
    list_editable = ('price', 'active')
    list_filter = ('category', 'active')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (
        ProductImageInline,
    )
    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'active', 'updated')
    list_editable = ('active',)
    list_filter = ('active',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('updated', 'timestamp')
    class Meta:
        model = Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(ProductImage)
