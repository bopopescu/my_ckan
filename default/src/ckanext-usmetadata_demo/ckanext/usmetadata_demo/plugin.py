'''
Created on Feb 9, 2015

@author: tthakur
'''
import ckan.plugins as p
import ckan.plugins.toolkit as tk


class MyPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)
    
    #add all the extra fields here
    def _modify_package_schema(self, schema):
        schema.update({
            'custom_text': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')], 
            'custom_text-1': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text-2': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        return schema
    
    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(MyPlugin, self).create_package_schema()
        #our custom field
        schema = self._modify_package_schema(schema)
        return schema
    
    def update_package_schema(self):
        schema = super(MyPlugin, self).update_package_schema()
        #our custom field
        schema = self._modify_package_schema(schema)
        return schema
    
    def show_package_schema(self):
        schema = super(MyPlugin, self).show_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
        '''schema.update({
            'custom_text': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        return schema'''
    
    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    
    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')