Name:		texlive-collection-metapost
Epoch:		1
Version:	72550
Release:	1
Summary:	MetaPost and Metafont packages
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-metapost.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-automata
Requires:	texlive-bbcard
Requires:	texlive-blockdraw_mp
Requires:	texlive-bpolynomial
Requires:	texlive-cmarrows
Requires:	texlive-drv
Requires:	texlive-dviincl
Requires:	texlive-emp
Requires:	texlive-epsincl
Requires:	texlive-expressg
Requires:	texlive-exteps
Requires:	texlive-featpost
Requires:	texlive-feynmf
Requires:	texlive-feynmp-auto
Requires:	texlive-garrigues
Requires:	texlive-gmp
Requires:	texlive-hatching
Requires:	texlive-latexmp
Requires:	texlive-metago
Requires:	texlive-metaobj
Requires:	texlive-metaplot
Requires:	texlive-metapost
Requires:	texlive-metauml
Requires:	texlive-mfpic
Requires:	texlive-mfpic4ode
Requires:	texlive-mp3d
Requires:	texlive-mpcolornames
Requires:	texlive-mpattern
Requires:	texlive-mpgraphics
Requires:	texlive-piechartmp
Requires:	texlive-repere
Requires:	texlive-roex
Requires:	texlive-slideshow
Requires:	texlive-splines
Requires:	texlive-suanpan
Requires:	texlive-textpath
Requires:	texlive-threeddice

%description
TeXLive collection-metapost package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
