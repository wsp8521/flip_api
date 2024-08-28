from rest_framework import permissions

class GenerePermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in ['GET','OPTIONS','HEAD']: #Vefi
            return request.user.has_perm('catalogoFilmes.view_genre') #permissão para visualizar
        
        if request.method =='POST':
            return request.user.has_perm('catalogoFilmes.add_genre') #permissão para adicionar
        
        if request.method in ['PUT','PATCH']:
            return request.user.has_perm('catalogoFilmes.change_genre') #permissão para alterar
        
        if request.method =='DELETE':
            return request.user.has_perm('catalogoFilmes.delete_genre') #permissão para deletar

        return False