# haversine-sinus-distance-measuring
Calculating Geographic Distances Through Haversine Approach

The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes. Important in navigation, it is a special case of a more general formula in spherical trigonometry, the law of haversines, that relates the sides and angles of spherical triangles.

The first table of haversines in English was published by James Andrew in 1805, but Florian Cajori credits an earlier use by José de Mendoza y Ríos in 1801.[The term haversine was coined in 1835 by James Inman.

These names follow from the fact that they are customarily written in terms of the haversine function, given by <span class="texhtml">hav(<i>θ</i>) = sin<sup>2</sup>(<span role="math" class="sfrac nowrap tion" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span class="num" style="display:block; line-height:1em; margin:0 0.1em;"><i>θ</i></span><span class="slash visualhide">/</span><span class="den" style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">2</span></span>)</span>. The formulas could equally be written in terms of any multiple of the haversine, such as the older versine function (twice the haversine). Prior to the advent of computers, the elimination of division and multiplication by factors of two proved convenient enough that tables of haversine values and logarithms were included in 19th- and early 20th-century navigation and trigonometric texts. These days, the haversine form is also convenient in that it has no coefficient in front of the <span class="texhtml">sin<sup>2</sup></span> function.


<h2><span class="mw-headline" id="Formulation">Formulation</span><span class="mw-editsection"><span class="mw-editsection-bracket"></span></h2>
<p>Let the <a href="/wiki/Central_angle" title="Central angle">central angle</a> <span class="texhtml">Θ</span> between any two points on a sphere be:
</p>
<dl><dd><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \Theta ={\frac {d}{r}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi mathvariant="normal">Θ<!-- Θ --></mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mi>d</mi>
            <mi>r</mi>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \Theta ={\frac {d}{r}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/46ef84e1563f06af1f55a089c6d301797be208bd" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -1.838ex; width:6.959ex; height:5.343ex;" alt="{\displaystyle \Theta ={\frac {d}{r}}}"></span></dd></dl>
<p>where:
</p>
<ul><li><span class="texhtml"><i>d</i></span> is the distance between the two points along a <a href="/wiki/Great_circle" title="Great circle">great circle</a> of the sphere (see <a href="/wiki/Great-circle_distance" title="Great-circle distance">spherical distance</a>),</li>
<li><span class="texhtml"><i>r</i></span> is the radius of the sphere.</li></ul>
<p>The <i>haversine formula</i> allows the <a href="/wiki/Haversine_function" class="mw-redirect" title="Haversine function">haversine</a> of <span class="texhtml">Θ</span> (that is, <span class="texhtml">hav(Θ)</span>) to be computed directly from the latitude and longitude of the two points:
</p>
<dl><dd><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \operatorname {hav} \left(\Theta \right)=\operatorname {hav} \left(\varphi _{2}-\varphi _{1}\right)+\cos \left(\varphi _{1}\right)\cos \left(\varphi _{2}\right)\operatorname {hav} \left(\lambda _{2}-\lambda _{1}\right)}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>hav</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mrow>
          <mo>(</mo>
          <mi mathvariant="normal">Θ<!-- Θ --></mi>
          <mo>)</mo>
        </mrow>
        <mo>=</mo>
        <mi>hav</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mrow>
          <mo>(</mo>
          <mrow>
            <msub>
              <mi>φ<!-- φ --></mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msub>
            <mo>−<!-- − --></mo>
            <msub>
              <mi>φ<!-- φ --></mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>1</mn>
              </mrow>
            </msub>
          </mrow>
          <mo>)</mo>
        </mrow>
        <mo>+</mo>
        <mi>cos</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mrow>
          <mo>(</mo>
          <msub>
            <mi>φ<!-- φ --></mi>
            <mrow class="MJX-TeXAtom-ORD">
              <mn>1</mn>
            </mrow>
          </msub>
          <mo>)</mo>
        </mrow>
        <mi>cos</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mrow>
          <mo>(</mo>
          <msub>
            <mi>φ<!-- φ --></mi>
            <mrow class="MJX-TeXAtom-ORD">
              <mn>2</mn>
            </mrow>
          </msub>
          <mo>)</mo>
        </mrow>
        <mi>hav</mi>
        <mo>⁡<!-- ⁡ --></mo>
        <mrow>
          <mo>(</mo>
          <mrow>
            <msub>
              <mi>λ<!-- λ --></mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msub>
            <mo>−<!-- − --></mo>
            <msub>
              <mi>λ<!-- λ --></mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>1</mn>
              </mrow>
            </msub>
          </mrow>
          <mo>)</mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \operatorname {hav} \left(\Theta \right)=\operatorname {hav} \left(\varphi _{2}-\varphi _{1}\right)+\cos \left(\varphi _{1}\right)\cos \left(\varphi _{2}\right)\operatorname {hav} \left(\lambda _{2}-\lambda _{1}\right)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/6c6913fe71d3ae1920334521f899e9b8e5615eb7" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:55.635ex; height:2.843ex;" alt="{\displaystyle \operatorname {hav} \left(\Theta \right)=\operatorname {hav} \left(\varphi _{2}-\varphi _{1}\right)+\cos \left(\varphi _{1}\right)\cos \left(\varphi _{2}\right)\operatorname {hav} \left(\lambda _{2}-\lambda _{1}\right)}"></span></dd></dl>

<p>where
</p>
<ul><li><span class="texhtml"><i>φ</i><sub>1</sub></span>, <span class="texhtml"><i>φ</i><sub>2</sub></span> are the latitude of point 1 and latitude of point 2 (in radians),</li>
<li><span class="texhtml"><i>λ</i><sub>1</sub></span>, <span class="texhtml"><i>λ</i><sub>2</sub></span> are the longitude of point 1 and longitude of point 2 (in radians).</li></ul>
<p>Finally, the <a href="/wiki/Haversine_function" class="mw-redirect" title="Haversine function">haversine function</a> <span class="texhtml">hav(Θ)</span>, applied above to both the central angle <span class="texhtml">Θ</span> and the differences in latitude and longitude, is
</p>
<dl><dd><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML"  alttext="{\displaystyle \operatorname {hav} (\theta )=\sin ^{2}\left({\frac {\theta }{2}}\right)={\frac {1-\cos(\theta )}{2}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>hav</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>&#x03B8;<!-- θ --></mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <msup>
          <mi>sin</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msup>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mrow>
          <mo>(</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mfrac>
              <mi>&#x03B8;<!-- θ --></mi>
              <mn>2</mn>
            </mfrac>
          </mrow>
          <mo>)</mo>
        </mrow>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mn>1</mn>
              <mo>&#x2212;<!-- − --></mo>
              <mi>cos</mi>
              <mo>&#x2061;<!-- ⁡ --></mo>
              <mo stretchy="false">(</mo>
              <mi>&#x03B8;<!-- θ --></mi>
              <mo stretchy="false">)</mo>
            </mrow>
            <mn>2</mn>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \operatorname {hav} (\theta )=\sin ^{2}\left({\frac {\theta }{2}}\right)={\frac {1-\cos(\theta )}{2}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7f6323f8e404496c8253539689327f5228699935" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.505ex; width:32.959ex; height:6.343ex;" alt="{\displaystyle \operatorname {hav} (\theta )=\sin ^{2}\left({\frac {\theta }{2}}\right)={\frac {1-\cos(\theta )}{2}}}"/></span></dd></dl>
<p>The haversine function computes half a <a href="/wiki/Versine" title="Versine">versine</a> of the angle <span class="texhtml"><i>θ</i></span>.
</p><p>To solve for the distance <span class="texhtml"><i>d</i></span>, apply the archaversine (<a href="/wiki/Inverse_haversine" class="mw-redirect" title="Inverse haversine">inverse haversine</a>) to <span class="texhtml"><i>h</i> = hav(Θ)</span> or use the <a href="/wiki/Arcsine" class="mw-redirect" title="Arcsine">arcsine</a> (inverse sine) function:
</p>
<dl><dd><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML"  alttext="{\displaystyle d=r\operatorname {archav} (h)=2r\arcsin \left({\sqrt {h}}\right)}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>d</mi>
        <mo>=</mo>
        <mi>r</mi>
        <mi>archav</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>h</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mn>2</mn>
        <mi>r</mi>
        <mi>arcsin</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mrow>
          <mo>(</mo>
          <mrow class="MJX-TeXAtom-ORD">
            <msqrt>
              <mi>h</mi>
            </msqrt>
          </mrow>
          <mo>)</mo>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle d=r\operatorname {archav} (h)=2r\arcsin \left({\sqrt {h}}\right)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/cbf447ff0f78607610cbd243d70845f01cb553cf" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -1.005ex; width:32.751ex; height:3.343ex;" alt="{\displaystyle d=r\operatorname {archav} (h)=2r\arcsin \left({\sqrt {h}}\right)}"/></span></dd></dl>
<p>or more explicitly:
</p>
<dl><dd><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML"  alttext="{\displaystyle {\begin{aligned}d&amp;=2r\arcsin \left({\sqrt {\operatorname {hav} (\varphi _{2}-\varphi _{1})+\cos(\varphi _{1})\cos(\varphi _{2})\operatorname {hav} (\lambda _{2}-\lambda _{1})}}\right)\\&amp;=2r\arcsin \left({\sqrt {\sin ^{2}\left({\frac {\varphi _{2}-\varphi _{1}}{2}}\right)+\cos(\varphi _{1})\cos(\varphi _{2})\sin ^{2}\left({\frac {\lambda _{2}-\lambda _{1}}{2}}\right)}}\right)\end{aligned}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mtable columnalign="right left right left right left right left right left right left" rowspacing="3pt" columnspacing="0em 2em 0em 2em 0em 2em 0em 2em 0em 2em 0em" displaystyle="true">
            <mtr>
              <mtd>
                <mi>d</mi>
              </mtd>
              <mtd>
                <mi></mi>
                <mo>=</mo>
                <mn>2</mn>
                <mi>r</mi>
                <mi>arcsin</mi>
                <mo>&#x2061;<!-- ⁡ --></mo>
                <mrow>
                  <mo>(</mo>
                  <mrow class="MJX-TeXAtom-ORD">
                    <msqrt>
                      <mi>hav</mi>
                      <mo>&#x2061;<!-- ⁡ --></mo>
                      <mo stretchy="false">(</mo>
                      <msub>
                        <mi>&#x03C6;<!-- φ --></mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msub>
                      <mo>&#x2212;<!-- − --></mo>
                      <msub>
                        <mi>&#x03C6;<!-- φ --></mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>1</mn>
                        </mrow>
                      </msub>
                      <mo stretchy="false">)</mo>
                      <mo>+</mo>
                      <mi>cos</mi>
                      <mo>&#x2061;<!-- ⁡ --></mo>
                      <mo stretchy="false">(</mo>
                      <msub>
                        <mi>&#x03C6;<!-- φ --></mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>1</mn>
                        </mrow>
                      </msub>
                      <mo stretchy="false">)</mo>
                      <mi>cos</mi>
                      <mo>&#x2061;<!-- ⁡ --></mo>
                      <mo stretchy="false">(</mo>
                      <msub>
                        <mi>&#x03C6;<!-- φ --></mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msub>
                      <mo stretchy="false">)</mo>
                      <mi>hav</mi>
                      <mo>&#x2061;<!-- ⁡ --></mo>
                      <mo stretchy="false">(</mo>
                      <msub>
                        <mi>&#x03BB;<!-- λ --></mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msub>
                      <mo>&#x2212;<!-- − --></mo>
                      <msub>
                        <mi>&#x03BB;<!-- λ --></mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>1</mn>
                        </mrow>
                      </msub>
                      <mo stretchy="false">)</mo>
                    </msqrt>
                  </mrow>
                  <mo>)</mo>
                </mrow>
              </mtd>
            </mtr>
            <mtr>
              <mtd />
              <mtd>
                <mi></mi>
                <mo>=</mo>
                <mn>2</mn>
                <mi>r</mi>
                <mi>arcsin</mi>
                <mo>&#x2061;<!-- ⁡ --></mo>
                <mrow>
                  <mo>(</mo>
                  <mrow class="MJX-TeXAtom-ORD">
                    <msqrt>
                      <msup>
                        <mi>sin</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msup>
                      <mo>&#x2061;<!-- ⁡ --></mo>
                      <mrow>
                        <mo>(</mo>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mfrac>
                            <mrow>
                              <msub>
                                <mi>&#x03C6;<!-- φ --></mi>
                                <mrow class="MJX-TeXAtom-ORD">
                                  <mn>2</mn>
                                </mrow>
                              </msub>
                              <mo>&#x2212;<!-- − --></mo>
                              <msub>
                                <mi>&#x03C6;<!-- φ --></mi>
                                <mrow class="MJX-TeXAtom-ORD">
                                  <mn>1</mn>
                                </mrow>
                              </msub>
                            </mrow>
                            <mn>2</mn>
                          </mfrac>
                        </mrow>
                        <mo>)</mo>
                      </mrow>
                      <mo>+</mo>
                      <mi>cos</mi>
                      <mo>&#x2061;<!-- ⁡ --></mo>
                      <mo stretchy="false">(</mo>
                      <msub>
                        <mi>&#x03C6;<!-- φ --></mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>1</mn>
                        </mrow>
                      </msub>
                      <mo stretchy="false">)</mo>
                      <mi>cos</mi>
                      <mo>&#x2061;<!-- ⁡ --></mo>
                      <mo stretchy="false">(</mo>
                      <msub>
                        <mi>&#x03C6;<!-- φ --></mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msub>
                      <mo stretchy="false">)</mo>
                      <msup>
                        <mi>sin</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msup>
                      <mo>&#x2061;<!-- ⁡ --></mo>
                      <mrow>
                        <mo>(</mo>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mfrac>
                            <mrow>
                              <msub>
                                <mi>&#x03BB;<!-- λ --></mi>
                                <mrow class="MJX-TeXAtom-ORD">
                                  <mn>2</mn>
                                </mrow>
                              </msub>
                              <mo>&#x2212;<!-- − --></mo>
                              <msub>
                                <mi>&#x03BB;<!-- λ --></mi>
                                <mrow class="MJX-TeXAtom-ORD">
                                  <mn>1</mn>
                                </mrow>
                              </msub>
                            </mrow>
                            <mn>2</mn>
                          </mfrac>
                        </mrow>
                        <mo>)</mo>
                      </mrow>
                    </msqrt>
                  </mrow>
                  <mo>)</mo>
                </mrow>
              </mtd>
            </mtr>
          </mtable>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle {\begin{aligned}d&amp;=2r\arcsin \left({\sqrt {\operatorname {hav} (\varphi _{2}-\varphi _{1})+\cos(\varphi _{1})\cos(\varphi _{2})\operatorname {hav} (\lambda _{2}-\lambda _{1})}}\right)\\&amp;=2r\arcsin \left({\sqrt {\sin ^{2}\left({\frac {\varphi _{2}-\varphi _{1}}{2}}\right)+\cos(\varphi _{1})\cos(\varphi _{2})\sin ^{2}\left({\frac {\lambda _{2}-\lambda _{1}}{2}}\right)}}\right)\end{aligned}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a65dbbde43ff45bacd2505fcf32b44fc7dcd8cc0" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -5.671ex; width:70.218ex; height:12.509ex;" alt="{\displaystyle {\begin{aligned}d&amp;=2r\arcsin \left({\sqrt {\operatorname {hav} (\varphi _{2}-\varphi _{1})+\cos(\varphi _{1})\cos(\varphi _{2})\operatorname {hav} (\lambda _{2}-\lambda _{1})}}\right)\\&amp;=2r\arcsin \left({\sqrt {\sin ^{2}\left({\frac {\varphi _{2}-\varphi _{1}}{2}}\right)+\cos(\varphi _{1})\cos(\varphi _{2})\sin ^{2}\left({\frac {\lambda _{2}-\lambda _{1}}{2}}\right)}}\right)\end{aligned}}}"/></span></dd></dl>
<p>When using these formulae, one must ensure that <span class="texhtml"><i>h</i></span> does not exceed 1 due to a <a href="/wiki/Floating_point" class="mw-redirect" title="Floating point">floating point</a> error (<span class="texhtml"><i>d</i></span> is only <a href="/wiki/Real_number" title="Real number">real</a> for <span class="texhtml">0 ≤ <i>h</i> ≤ 1</span>). <span class="texhtml"><i>h</i></span> only approaches 1 for <i>antipodal</i> points (on opposite sides of the sphere)—in this region, relatively large numerical errors tend to arise in the formula when finite precision is used. Because <span class="texhtml"><i>d</i></span> is then large (approaching <span class="texhtml">π<i>R</i></span>, half the circumference) a small error is often not a major concern in this unusual case (although there are other <a href="/wiki/Great-circle_distance" title="Great-circle distance">great-circle distance</a> formulas that avoid this problem).  (The formula above is sometimes written in terms of the <a href="/wiki/Arctangent" class="mw-redirect" title="Arctangent">arctangent</a> function, but this suffers from similar numerical problems near <span class="texhtml"><i>h</i> = 1</span>.)
</p><p>As described below, a similar formula can be written using cosines (sometimes called the <a href="/wiki/Spherical_law_of_cosines" title="Spherical law of cosines">spherical law of cosines</a>, not to be confused with the <a href="/wiki/Law_of_cosines" title="Law of cosines">law of cosines</a> for plane geometry) instead of haversines, but if the two points are close together (e.g. a kilometer apart, on the Earth) you might end up with <span class="texhtml">cos(<span role="math" class="sfrac nowrap tion" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span class="num" style="display:block; line-height:1em; margin:0 0.1em;"><i>d</i></span><span class="slash visualhide">/</span><span class="den" style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;"><i>R</i></span></span>) = 0.99999999</span>, leading to an inaccurate answer. Since the haversine formula uses sines, it avoids that problem.
</p><p>Either formula is only an approximation when applied to the <a href="/wiki/Earth" title="Earth">Earth</a>, which is not a perfect sphere: the "<a href="/wiki/Earth_radius" title="Earth radius">Earth radius</a>" <span class="texhtml"><i>R</i></span> varies from 6356.752&#160;km at the poles to 6378.137&#160;km at the equator.  More importantly, the <a href="/wiki/Radius_of_curvature_(applications)" class="mw-redirect" title="Radius of curvature (applications)">radius of curvature</a> of a north-south line on the earth's surface is 1% greater at the poles (≈6399.594&#160;km) than at the equator (≈6335.439&#160;km)&#8212;so the haversine formula and law of cosines cannot be guaranteed correct to better than 0.5%.<sup class="noprint Inline-Template Template-Fact" style="white-space:nowrap;">&#91;<i><a href="/wiki/Wikipedia:Citation_needed" title="Wikipedia:Citation needed"><span title="Your explanation here (January 2019)">citation needed</span></a></i>&#93;</sup> More accurate methods that consider the Earth's ellipticity are given by <a href="/wiki/Vincenty%27s_formulae" title="Vincenty&#39;s formulae">Vincenty's formulae</a> and the other formulas in the <a href="/wiki/Geographical_distance" title="Geographical distance">geographical distance</a> article.
</p>
<h2><span class="mw-headline" id="The_law_of_haversines">The law of haversines<span id="Law"></span></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Haversine_formula&amp;action=edit&amp;section=2" title="Edit section: The law of haversines">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Law-of-haversines.svg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Law-of-haversines.svg/220px-Law-of-haversines.svg.png" decoding="async" width="220" height="220" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Law-of-haversines.svg/330px-Law-of-haversines.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/38/Law-of-haversines.svg/440px-Law-of-haversines.svg.png 2x" data-file-width="231" data-file-height="231" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Law-of-haversines.svg" class="internal" title="Enlarge"></a></div>Spherical triangle solved by the law of haversines</div></div></div>
<p>Given a unit sphere, a "triangle" on the surface of the sphere is defined by the <a href="/wiki/Great_circle" title="Great circle">great circles</a> connecting three points <span class="texhtml"><i>u</i></span>, <span class="texhtml"><i>v</i></span>, and <span class="texhtml"><i>w</i></span> on the sphere.  If the lengths of these three sides are <span class="texhtml"><i>a</i></span> (from <span class="texhtml"><i>u</i></span> to <span class="texhtml"><i>v</i></span>), <span class="texhtml"><i>b</i></span> (from <span class="texhtml"><i>u</i></span> to <span class="texhtml"><i>w</i></span>), and <span class="texhtml"><i>c</i></span> (from <span class="texhtml"><i>v</i></span> to <span class="texhtml"><i>w</i></span>), and the angle of the corner opposite <span class="texhtml"><i>c</i></span> is <span class="texhtml"><i>C</i></span>, then the law of haversines states:<sup id="cite_ref-Korn_2000_9-0" class="reference"><a href="#cite_note-Korn_2000-9">&#91;9&#93;</a></sup>
</p>
<dl><dd><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML"  alttext="{\displaystyle \operatorname {hav} (c)=\operatorname {hav} (a-b)+\sin(a)\sin(b)\operatorname {hav} (C).}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>hav</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>c</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>hav</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>a</mi>
        <mo>&#x2212;<!-- − --></mo>
        <mi>b</mi>
        <mo stretchy="false">)</mo>
        <mo>+</mo>
        <mi>sin</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>a</mi>
        <mo stretchy="false">)</mo>
        <mi>sin</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>b</mi>
        <mo stretchy="false">)</mo>
        <mi>hav</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>C</mi>
        <mo stretchy="false">)</mo>
        <mo>.</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \operatorname {hav} (c)=\operatorname {hav} (a-b)+\sin(a)\sin(b)\operatorname {hav} (C).}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/106761cdc170f70bc88a524843b1eb997c27f06e" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:43.233ex; height:2.843ex;" alt="{\displaystyle \operatorname {hav} (c)=\operatorname {hav} (a-b)+\sin(a)\sin(b)\operatorname {hav} (C).}"/></span></dd></dl>
<p>Since this is a unit sphere, the lengths <span class="texhtml"><i>a</i></span>, <span class="texhtml"><i>b</i></span>, and <span class="texhtml"><i>c</i></span> are simply equal to the angles (in <a href="/wiki/Radian" title="Radian">radians</a>) subtended by those sides from the center of the sphere (for a non-unit sphere, each of these arc lengths is equal to its <a href="/wiki/Central_angle" title="Central angle">central angle</a> multiplied by the radius <span class="texhtml"><i>R</i></span> of the sphere).
</p><p>In order to obtain the haversine formula of the previous section from this law, one simply considers the special case where <span class="texhtml"><i>u</i></span> is the <a href="/wiki/Geographic_North_Pole" class="mw-redirect" title="Geographic North Pole">north pole</a>, while <span class="texhtml"><i>v</i></span> and <span class="texhtml"><i>w</i></span> are the two points whose separation <span class="texhtml"><i>d</i></span> is to be determined.  In that case, <span class="texhtml"><i>a</i></span> and <span class="texhtml"><i>b</i></span> are <span class="texhtml"><span role="math" class="sfrac nowrap tion" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span class="num" style="display:block; line-height:1em; margin:0 0.1em;">π</span><span class="slash visualhide">/</span><span class="den" style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">2</span></span> − <i>φ</i><sub>1,2</sub></span> (that is, the, co-latitudes), <span class="texhtml"><i>C</i></span> is the longitude separation <span class="texhtml"><i>λ</i><sub>2</sub> − <i>λ</i><sub>1</sub></span>, and <span class="texhtml"><i>c</i></span> is the desired <span class="texhtml"><span role="math" class="sfrac nowrap tion" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span class="num" style="display:block; line-height:1em; margin:0 0.1em;"><i>d</i></span><span class="slash visualhide">/</span><span class="den" style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;"><i>R</i></span></span></span>.  Noting that <span class="texhtml">sin(<span role="math" class="sfrac nowrap tion" style="display:inline-block; vertical-align:-0.5em; font-size:85%; text-align:center;"><span class="num" style="display:block; line-height:1em; margin:0 0.1em;">π</span><span class="slash visualhide">/</span><span class="den" style="display:block; line-height:1em; margin:0 0.1em; border-top:1px solid;">2</span></span> − <i>φ</i>) = cos(<i>φ</i>)</span>, the haversine formula immediately follows.
</p><p>To derive the law of haversines, one starts with the <a href="/wiki/Spherical_law_of_cosines" title="Spherical law of cosines">spherical law of cosines</a>:
</p>
<dl><dd><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML"  alttext="{\displaystyle \cos(c)=\cos(a)\cos(b)+\sin(a)\sin(b)\cos(C).\,}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>cos</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>c</mi>
        <mo stretchy="false">)</mo>
        <mo>=</mo>
        <mi>cos</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>a</mi>
        <mo stretchy="false">)</mo>
        <mi>cos</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>b</mi>
        <mo stretchy="false">)</mo>
        <mo>+</mo>
        <mi>sin</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>a</mi>
        <mo stretchy="false">)</mo>
        <mi>sin</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>b</mi>
        <mo stretchy="false">)</mo>
        <mi>cos</mi>
        <mo>&#x2061;<!-- ⁡ --></mo>
        <mo stretchy="false">(</mo>
        <mi>C</mi>
        <mo stretchy="false">)</mo>
        <mo>.</mo>
        <mspace width="thinmathspace" />
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \cos(c)=\cos(a)\cos(b)+\sin(a)\sin(b)\cos(C).\,}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0a9cb576d5f144c4e95919b4f41f9504c3ba8912" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:44.373ex; height:2.843ex;" alt="{\displaystyle \cos(c)=\cos(a)\cos(b)+\sin(a)\sin(b)\cos(C).\,}"/></span></dd></dl>
<p>As mentioned above, this formula is an ill-conditioned way of solving for <span class="texhtml"><i>c</i></span> when <span class="texhtml"><i>c</i></span> is small.  Instead, we substitute the identity that <span class="texhtml">cos(<i>θ</i>) = 1 − 2 hav(<i>θ</i>)</span>, and also employ the <a href="/wiki/Trigonometric_identity#Addition/subtraction_theorems" class="mw-redirect" title="Trigonometric identity">addition identity</a> <span class="texhtml">cos(<i>a</i> − <i>b</i>) = cos(<i>a</i>) cos(<i>b</i>) + sin(<i>a</i>) sin(<i>b</i>)</span>, to obtain the law of haversines, above.
</p>