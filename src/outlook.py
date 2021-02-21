#This file is part of sashay and may be subject to redistribution and commercial restrictions. Please visit our website
#for more information on licensing and terms of use.
#
#
import spinher
import quo
with spinher.whirl():
  quo.flair(f'CREATED BY GERRISHON SIRERE', bold=True, fg='bblack', bg='byellow')

class logo:
  @classmethod
  def tool_header(self):
    print('''\007

\033[1;33m                                                                                                            
                         888                       
                         888                      
     .oooo.o    .oooo.o  888888bo.   ooo    ooo
    d88(  "8   d88(  "8 o888888888b  `88.  .8'
   `"Y88b.    `"Y88b.    888    888    `88..8'
   o.  )88b   o.  )88b   888    888     `888'
   8""888P'   8""888P'  o888o  o888o    "888" 
                                         d8'
                                    .o...P' 




\033[1;36m %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;m
\033[1;33m |            INSTALL USEFUL TOOLS              |
\033[1;36m %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[00m''')

  @classmethod
  def tool_footer(self):
    quo.flair(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', fg='vivid_blue') 


  @classmethod
  def not_ins(self):
    self.tool_header()
    quo.echo(f'[ x ] sashay cannot be installed at the moment')
    quo.echo(f'[ x ] An error occurred, please try again later')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header() 
    quo.flair(f'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERRCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL I BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.', fg='vivid_black', bg='vivid_white')
    quo.flair(f'Installing this tool means you agree with all terms', bold=True, fg='vivid_red') 
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    quo.flair(f'[ ✓ ] sashay has been installed successfully', fg='white')
    quo.flair(f'[ ✓ ] Type sashay or sshy from anywhere in your terminal', fg='yellow') 
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    quo.flair(f'[ 1 ] Update sashay', bold=True, fg='vivid_blue')
    quo.flair(f'[ 0 ] << Go back', bold=True, fg='vivid_yellow')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    quo.flair(f'[ ✓ ] Congratulations! sashay has been updated successfully', fg='vivid_black', bg='vivid_green') 
    quo.flair(f'[ ✓ ] Press enter to continue', fg='vivid_green')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    quo.flair(f'[ x ] There is no network connectivity', bold=True, fg='white')
    quo.flair(f'[ x ] Please try again later', fg='white')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
\033[1;31m  [ x ]  \033[1;33msshy can't be updated at this time.\033[1;m
\033[1;31m  [ x ]  \033[1;31mPlease try again later.\033[00m''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    quo.flair(f'[✓] sashay', bold=True, fg='vivid_black', bg='vivid_yellow')
    quo.flair(f'[✓] By Gerrishon Sirere(viewerdiscretion)', fg='vivid_blue')
    quo.flair(f'[✓] With great power comes great responsibility', underline=True, fg='vivid_blue')
    quo.flair(f'[✓] 360+ tools', fg='red') 
    quo.flair(f'[✓] Made for Linux based systems', fg='blue') 

    self.tool_footer()


  @classmethod
  def install_tools(self):
    quo.flair(f'#############################################', fg='black', bg='cyan')
    quo.flair(f'//////////////SELECT YOUR TOOL///////////////', fg='red', bg='white') 
    quo.flair(f'#############################################', fg='black', bg='cyan')

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m is already Installed !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mInstalled successfully !!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m has been installed Successfully! 
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;31mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m has not been installed! 
''')
    self.tool_footer()

  @classmethod
  def back(self):
    quo.flair(f'#############################################', fg='vivid_black', bg='vivid_cyan')
    quo.flair(f'00) Go back', bold=True, fg='vivid_yellow') 
    quo.flair(f'#############################################', fg='vivid_black', bg='vivid_cyan')

  @classmethod
  def updating(self):
    quo.flair(f'#############################################', fg='vivid_black', bg='vivid_cyan')
    quo.flair(f'//////////////////UPDATING///////////////////', fg='vivid_red', bg='vivid_white') 
    quo.flair(f'#############################################', fg='vivid_black', bg='vivid_cyan')

  @classmethod
  def installing(self):
    quo.flair(f'#############################################', fg='vivid_black', bg='vivid_cyan')
    quo.flair(f'/////////////////INSTALLING//////////////////', fg='vivid_red', bg='vivid_white') 
    quo.flair(f'#############################################', fg='vivid_black', bg='vivid_cyan')

  @classmethod
  def menu(self,total):
    self.tool_header()
    quo.flair(f'[ 1 ] Show all tools', bold=True, bg='vivid_yellow', fg='vivid_black')
    quo.flair(f'[ 2 ] Show all categories', bold=True, bg='vivid_black', fg='vivid_yellow')
    quo.flair(f'[ 3 ] Update sashay', bold=True, fg='vivid_black', bg='vivid_yellow')
    quo.flair(f'[ 4 ] About us', bold=True, fg='vivid_yellow', bg='vivid_black')
    quo.flair(f'[ x ] Exit sashay', bold=True, fg='vivid_black', bg='vivid_yellow')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    quo.flair(f'We hope to see you back soon', fg='black', bg='vivid_red')
    quo.flair(f'Goodbye for now...', fg='white') 
    self.tool_footer()