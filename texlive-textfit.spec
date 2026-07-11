%global tl_name textfit
%global tl_revision 20591

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5
Release:	%{tl_revision}.1
Summary:	Fit text to a desired size
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/textfit
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textfit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textfit.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textfit.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Package to fit text to a given width or height by scaling the font. For
example: \scaletowidth{3in}{This}. (The job is done by calculating a
magstep and applying it to the current font; thus "This" will be very
tall, as well as very wide; to scale in just one dimension, use the
facilities of the graphicx package.)

