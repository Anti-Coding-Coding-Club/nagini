from .admin_commands import NaginiAdminCog
from .nagini_commands import NaginiCommandsCog

def setup(nagini):
    nagini.add_cog(NaginiAdminCog(nagini))
    nagini.add_cog(NaginiCommandsCog(nagini))