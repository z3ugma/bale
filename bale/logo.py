from nicegui import ui
import logging

logger = logging.getLogger(__name__)

# https://www.svgviewer.dev/s/130897/turtle
logo = """
<svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 42 42">
<path fill="#E48257" d="m26.001 26.422-3.594 2.075v7.209c3.739-.449 7.072-2.704 9.135-6.086l-5.541-3.199zm-16.749-9.67a15.142 15.142 0 0 0 0 10.339l5.359-3.094v-4.151c-4.116-2.375-2.764-1.595-5.359-3.094zm1.219-2.529c2.578 1.488 2.013 1.161 5.54 3.199l3.594-2.075v-7.21c-3.62.435-7.014 2.603-9.135 6.086zm5.54 12.199-5.541 3.2c2.018 3.308 5.321 5.627 9.136 6.085v-7.209l-3.594-2.075zm4.994-8.65-3.594 2.075v4.151l3.594 2.075 3.594-2.075v-4.151zm1.4-9.634v7.209l3.594 2.075 5.54-3.199c-2.02-3.321-5.339-5.629-9.134-6.086zm10.354 8.615L27.4 19.847v4.151l5.359 3.094a15.142 15.142 0 0 0 0-10.339zM21.006 0c-2.752 0-5.178 1.862-5.178 6.211a14.479 14.479 0 0 1 10.357-.001c0-4.223-2.316-6.21-5.179-6.21zm11.157 10.374c2.031 2.285 3.392 5.104 3.976 8.106l.012.066c6.414-3.641 1.456-11.252-3.988-8.173zm3.918 15.272-.01.05c-.637 2.968-2.045 5.774-4.15 8.037 5.27 3.144 10.511-4.294 4.16-8.088zM5.86 18.547c.626-3.007 1.827-5.752 3.989-8.172C4.471 7.322-.615 14.871 5.86 18.547zm.071 7.099c-6.313 3.771-1.195 11.283 4.161 8.088-2.23-2.384-3.761-5.682-4.161-8.088zm12.513 12.715 1.29 2.822c.498 1.09 2.049 1.088 2.546 0l1.29-2.822a14.496 14.496 0 0 1-5.126 0z"/>
</svg>"""

# favicon = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAAXNSR0IArs4c6QAABINJREFUaEPVWj1oVEEQnr0IF87WWKTwp1OjjSA2EdMYNHhgcWvAUjvFwkZLtbSyEO20FOJLIVwwok1EGxFsNNHKaAoLtfXIgbkn3/PmHCe7b9/L7al5TSDv7cx88/PN7O4ZKvBMT0/vXVtbqxtjjhDRWJqmo8aYaoGlhT9J07RtjPlMRItpmj4fGhpqzszMvAsJMHkfWGuPEdElIjoREjSg9/NEdDNJkqc++U4A9Xq9Vq1Wbxljzg7IsFJi0zS91263LzabzZZeuA6AtfYAEd0nov2ltAz+47dEdCZJkjdS1R8AusY/JqLRGPZsqXQyMT86lRjiIAM1clyC6AFA2gwPD7+M4fmJHR/p/MFXPaO/trbSwsouSt7viwHk7erq6mFOpx6ARqNxN0bO2z1LZPcsOg0FiDuvD/UNAjUxOzt7DoIyAF22edKv5JHad7o9+cgrBpEAgMVvI/2qwvpJsBMDgNa+qVKnjsvK5P1YrFSaT5JkyqBJdTqdpRguQd4DBB54+0urlv0d2/aVEB08sdIIsiqVyj7TaDQuG2NuxAAAQ/G4UgQAttd+0XikFKI0Ta8Ya22TiE7GAPAPZMwBwAci2h1LOTw9seNTljLMOGAmPEvfRqJ5v2vvMlJotchgFkoBvEcNyDS6/mIi03N1fKH3/zwmCunQTs4GQGttmud9bZirEGXxsizkuQsAv9dspPsHgF57cTQjgbwnCEB6jwWdfmh7Ml3vuVDzADBTXXgylcmCo66NP+uxlX7vA5ELwMXrMIpZxGd8UQA6miF9LhC5AHRYZVog1wHA94RSSK5DsaM/4NHpGOobpQBI7zPbFJl7fJFyDXnaMaHOnQtAzzYy99mDLiBaaZFvZEQkYNRIXiEHi5jzUoYSChB2KRhGIuUwMvsUMhDdD3it7BuIrEytDRWx9DLGAC7eB6eSzEiAWljZ6TSYjYIMHygZGchjRsobSTSQYAT0Ap1Wrjx2cbre0Lj2DbLGcslfvCwNwDcyc67msRMb6Ns3/BUAvh1XDAAhxindB1wLBgmgSNH2XQO+FCkSAf7Gl0J/BYBWDmZyUaqcTF0TKLMU7+Dg2RDnbziFeMzVNBraoMO4kVordw8shzhulIgyb0dDbBRkIU4ZOdvAMJ5dWAFqg//vO//xfaMdxNGDHK2ndA3gmAQKZKORQlw1oVMG38Ao3tjzqOw77EKjHMg4rYc5mefaM0WnUb1x0X0m1BtK7QdkFEKHWEUBAHjeHiPETKWm0SIbEI5EUQDSeFePCTFTcFPv2u+GlAJEEQCy87pqScpwsRFv6nOPVVyzvBbsKtI8AK6+oB1VcKxYLnywxVTn42cN1AUgdMwe0uGIwlzUo0Xf/gHMAkChI5JQ09Lvs6PFmIe7ZQ3o9/vscBdCrLVRjtelQbJpcVPq12C1/tfxehcArlP7vuCQKaQvOkJ0uAFwvy84sDjWFRMbIlkldLZT1vh1V0wQEPOSD/Jkp47sffclXzeVcEcc9Zo14hUrTPRfs3IYN/VFN4PY1D81kAW1aX/soVnhf/65zU8sHJ18FN1uYgAAAABJRU5ErkJggg=="
favicon = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-3 -3 48 48" style="enable-background:new -3 -3 48 48" xml:space="preserve" width="42" height="42">
<rect x="-3" y="-3" height="48" width="48" rx="3" ry="3"/>
<path fill="#E48257" d="m26.001 26.422-3.594 2.075v7.209c3.739-.449 7.072-2.704 9.135-6.086l-5.541-3.199zm-16.749-9.67a15.142 15.142 0 0 0 0 10.339l5.359-3.094v-4.151c-4.116-2.375-2.764-1.595-5.359-3.094zm1.219-2.529c2.578 1.488 2.013 1.161 5.54 3.199l3.594-2.075v-7.21c-3.62.435-7.014 2.603-9.135 6.086zm5.541 12.199-5.541 3.2c2.018 3.308 5.321 5.627 9.136 6.085v-7.209l-3.594-2.075zm4.994-8.651-3.594 2.075v4.151l3.594 2.075 3.595-2.075v-4.151Zm1.4-9.634v7.209L26 17.421l5.54-3.199c-2.02-3.321-5.339-5.629-9.134-6.086zm10.354 8.615-5.359 3.094v4.151l5.359 3.094a15.142 15.142 0 0 0 0-10.339zM21.006 0c-2.752 0-5.178 1.862-5.178 6.211a14.479 14.479 0 0 1 10.357-.001c0-4.223-2.316-6.21-5.179-6.21zm11.158 10.374c2.031 2.285 3.392 5.104 3.976 8.106l.012.066c6.414-3.641 1.456-11.252-3.988-8.173zm3.918 15.272-.01.05c-.637 2.968-2.045 5.774-4.15 8.037 5.27 3.144 10.511-4.294 4.16-8.088zM5.86 18.547c.626-3.007 1.827-5.752 3.989-8.172C4.471 7.322-.615 14.871 5.86 18.547zm.071 7.099c-6.313 3.771-1.195 11.283 4.161 8.088-2.23-2.384-3.761-5.682-4.161-8.088zm12.512 12.715 1.29 2.822c.498 1.09 2.049 1.088 2.546 0l1.29-2.822a14.496 14.496 0 0 1-5.126 0z"/></svg>
"""


def show():
    ui.html(logo)
